from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solidworks_com import SolidWorks, mm


@dataclass(frozen=True)
class InvoluteTestSpec:
    teeth: int = 8
    module: float = mm(5.0)
    pressure_angle: float = math.radians(20.0)
    backlash: float = mm(0.05)

    @property
    def pitch_radius(self) -> float:
        return 0.5 * self.module * self.teeth

    @property
    def base_radius(self) -> float:
        return self.pitch_radius * math.cos(self.pressure_angle)

    @property
    def outer_radius(self) -> float:
        return self.pitch_radius + self.module

    @property
    def root_radius(self) -> float:
        return self.pitch_radius - 1.25 * self.module


def involute_function_angle(angle: float) -> float:
    return math.tan(angle) - angle


def expression(value: float) -> str:
    return f"{value:.12g}"


def rotated_involute_expressions(base_radius: float, rotation: float, *, mirror: bool = False) -> tuple[str, str]:
    rb = expression(base_radius)
    c = expression(math.cos(rotation))
    s = expression(math.sin(rotation))
    raw_x = f"({rb})*(cos(t)+t*sin(t))"
    raw_y = f"({rb})*(sin(t)-t*cos(t))"
    if mirror:
        raw_y = f"-({raw_y})"
    x_expr = f"({raw_x})*({c})-({raw_y})*({s})"
    y_expr = f"({raw_x})*({s})+({raw_y})*({c})"
    return x_expr, y_expr


def involute_point(base_radius: float, t: float, rotation: float, *, mirror: bool = False) -> tuple[float, float]:
    x = base_radius * (math.cos(t) + t * math.sin(t))
    y = base_radius * (math.sin(t) - t * math.cos(t))
    if mirror:
        y = -y
    c = math.cos(rotation)
    s = math.sin(rotation)
    return x * c - y * s, x * s + y * c


def polar_point(radius: float, angle: float) -> tuple[float, float]:
    return radius * math.cos(angle), radius * math.sin(angle)


def draw_arc_by_angles(sk, radius: float, start_angle: float, end_angle: float) -> None:
    mid_angle = 0.5 * (start_angle + end_angle)
    start = polar_point(radius, start_angle)
    end = polar_point(radius, end_angle)
    mid = polar_point(radius, mid_angle)
    sk.three_point_arc(start[0], start[1], end[0], end[1], mid[0], mid[1])


def build_equation_involute_test(
    output_dir: Path,
    visible: bool = True,
    reference_circles: bool = False,
    tooth_outline: bool = False,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    spec = InvoluteTestSpec()
    sw = SolidWorks.connect(visible=visible)
    part = sw.new_part()

    base_to_outer_t = math.sqrt((spec.outer_radius / spec.base_radius) ** 2 - 1.0)
    half_tooth_angle = math.pi / (2.0 * spec.teeth) - spec.backlash / (2.0 * spec.pitch_radius)
    flank_rotation = half_tooth_angle + involute_function_angle(spec.pressure_angle)

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        if reference_circles:
            sk.circle(0.0, 0.0, spec.root_radius)
            sk.circle(0.0, 0.0, spec.base_radius)
            sk.circle(0.0, 0.0, spec.pitch_radius)
            sk.circle(0.0, 0.0, spec.outer_radius)

        right_x, right_y = rotated_involute_expressions(spec.base_radius, flank_rotation, mirror=True)
        left_x, left_y = rotated_involute_expressions(spec.base_radius, -flank_rotation)
        sk.equation_spline(
            right_x,
            right_y,
            range_start="0",
            range_end=expression(base_to_outer_t),
            lock_start=True,
            lock_end=True,
        )
        sk.equation_spline(
            left_x,
            left_y,
            range_start="0",
            range_end=expression(base_to_outer_t),
            lock_start=True,
            lock_end=True,
        )

        if tooth_outline:
            right_base = involute_point(spec.base_radius, 0.0, flank_rotation, mirror=True)
            right_tip = involute_point(spec.base_radius, base_to_outer_t, flank_rotation, mirror=True)
            left_base = involute_point(spec.base_radius, 0.0, -flank_rotation)
            left_tip = involute_point(spec.base_radius, base_to_outer_t, -flank_rotation)

            right_base_angle = math.atan2(right_base[1], right_base[0])
            right_tip_angle = math.atan2(right_tip[1], right_tip[0])
            left_base_angle = math.atan2(left_base[1], left_base[0])
            left_tip_angle = math.atan2(left_tip[1], left_tip[0])

            right_root = polar_point(spec.root_radius, right_base_angle)
            left_root = polar_point(spec.root_radius, left_base_angle)
            sk.line(right_root[0], right_root[1], 0.0, right_base[0], right_base[1], 0.0)
            draw_arc_by_angles(sk, spec.outer_radius, right_tip_angle, left_tip_angle)
            sk.line(left_base[0], left_base[1], 0.0, left_root[0], left_root[1], 0.0)
            draw_arc_by_angles(sk, spec.root_radius, left_base_angle, right_base_angle)

    part.rebuild()
    path = output_dir / "equation_involute_exaggerated_test.SLDPRT"
    part.save_as(path)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an equation-driven involute curve test part in SOLIDWORKS.")
    parser.add_argument("--output-dir", type=Path, default=Path("output") / "gears")
    parser.add_argument("--hidden", action="store_true", help="Run SOLIDWORKS without making the window visible.")
    parser.add_argument("--reference-circles", action="store_true", help="Also draw root, base, pitch, and outside circles.")
    parser.add_argument("--tooth-outline", action="store_true", help="Also draw root/tip arcs and root connection lines.")
    args = parser.parse_args()

    path = build_equation_involute_test(
        args.output_dir,
        visible=not args.hidden,
        reference_circles=args.reference_circles,
        tooth_outline=args.tooth_outline,
    )
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()
