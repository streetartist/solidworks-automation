from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solidworks_com import SolidWorks, SolidWorksError, mm


@dataclass(frozen=True)
class SpurGearSpec:
    name: str
    teeth: int
    module: float = mm(2.0)
    pressure_angle: float = math.radians(20.0)
    thickness: float = mm(8.0)
    addendum_factor: float = 1.0
    dedendum_factor: float = 1.25
    backlash: float = mm(0.05)
    bore_radius: float = mm(5.0)
    involute_steps: int = 22
    root_steps: int = 24
    tip_steps: int = 10
    root_fillet_steps: int = 12

    @property
    def pitch_radius(self) -> float:
        return 0.5 * self.module * self.teeth

    @property
    def base_radius(self) -> float:
        return self.pitch_radius * math.cos(self.pressure_angle)

    @property
    def outer_radius(self) -> float:
        return self.pitch_radius + self.addendum_factor * self.module

    @property
    def cutter_outer_radius(self) -> float:
        return self.outer_radius + 0.75 * self.module

    @property
    def root_radius(self) -> float:
        return self.pitch_radius - self.dedendum_factor * self.module


def polar(point: tuple[float, float]) -> tuple[float, float]:
    x, y = point
    return math.hypot(x, y), math.atan2(y, x)


def rotate(point: tuple[float, float], angle: float) -> tuple[float, float]:
    x, y = point
    c = math.cos(angle)
    s = math.sin(angle)
    return x * c - y * s, x * s + y * c


def involute_angle(pressure_angle: float) -> float:
    return math.tan(pressure_angle) - pressure_angle


def expression(value: float) -> str:
    return f"{value:.12g}"


def expression_mm(value: float) -> str:
    return expression(value * 1000.0)


def point_at(radius: float, angle: float, center: tuple[float, float], rotation: float) -> tuple[float, float]:
    x = radius * math.cos(angle + rotation) + center[0]
    y = radius * math.sin(angle + rotation) + center[1]
    return x, y


def arc_points(
    radius: float,
    start_angle: float,
    end_angle: float,
    count: int,
    center: tuple[float, float],
    rotation: float,
    *,
    include_start: bool = False,
) -> list[tuple[float, float]]:
    first = 0 if include_start else 1
    return [
        point_at(radius, start_angle + (end_angle - start_angle) * i / count, center, rotation)
        for i in range(first, count + 1)
    ]


def radial_blend_points(
    root_radius: float,
    base_radius: float,
    angle: float,
    count: int,
    center: tuple[float, float],
    rotation: float,
    *,
    include_start: bool = False,
) -> list[tuple[float, float]]:
    first = 0 if include_start else 1
    points: list[tuple[float, float]] = []
    for index in range(first, count + 1):
        t = index / count
        smooth = t * t * (3.0 - 2.0 * t)
        radius = root_radius + (base_radius - root_radius) * smooth
        points.append(point_at(radius, angle, center, rotation))
    return points


def flank_points(
    spec: SpurGearSpec,
    mirror: bool,
    center: tuple[float, float],
    rotation: float,
) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for index in range(spec.involute_steps + 1):
        radius = spec.base_radius + (spec.outer_radius - spec.base_radius) * index / spec.involute_steps
        pressure_at_radius = math.acos(spec.base_radius / radius)
        half_angle = (
            math.pi / (2.0 * spec.teeth)
            + involute_angle(spec.pressure_angle)
            - involute_angle(pressure_at_radius)
            - spec.backlash / (2.0 * spec.pitch_radius)
        )
        angle = -half_angle if mirror else half_angle
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        x, y = rotate((x, y), rotation)
        points.append((x + center[0], y + center[1]))
    return points


def transformed(points: list[tuple[float, float]], center: tuple[float, float], rotation: float) -> list[tuple[float, float]]:
    result: list[tuple[float, float]] = []
    for point in points:
        x, y = rotate(point, rotation)
        result.append((x + center[0], y + center[1]))
    return result


def append_points(target: list[tuple[float, float]], points: list[tuple[float, float]], *, tolerance: float = 1e-9) -> None:
    for point in points:
        if target and math.dist(target[-1], point) <= tolerance:
            continue
        target.append(point)


def gear_profile_points(
    spec: SpurGearSpec,
    *,
    center: tuple[float, float] = (0.0, 0.0),
    rotation: float = 0.0,
) -> list[tuple[float, float]]:
    right = flank_points(spec, mirror=False, center=(0.0, 0.0), rotation=0.0)
    left = flank_points(spec, mirror=True, center=(0.0, 0.0), rotation=0.0)
    right_base_angle = polar(right[0])[1]
    right_tip_angle = polar(right[-1])[1]
    left_base_angle = polar(left[0])[1]
    left_tip_angle = polar(left[-1])[1]
    tooth_pitch = 2.0 * math.pi / spec.teeth

    points: list[tuple[float, float]] = []
    for tooth in range(spec.teeth):
        tooth_angle = tooth * tooth_pitch
        next_tooth_angle = (tooth + 1) * tooth_pitch

        if tooth == 0:
            points.append(point_at(spec.root_radius, left_base_angle, center, rotation))

        append_points(
            points,
            radial_blend_points(
                spec.root_radius,
                spec.base_radius,
                left_base_angle + tooth_angle,
                spec.root_fillet_steps,
                center,
                rotation,
            ),
        )
        append_points(points, transformed(left[1:], center, tooth_angle + rotation))
        append_points(
            points,
            arc_points(
                spec.outer_radius,
                left_tip_angle + tooth_angle,
                right_tip_angle + tooth_angle,
                spec.tip_steps,
                center,
                rotation,
            ),
        )
        append_points(points, transformed(list(reversed(right))[1:], center, tooth_angle + rotation))
        append_points(
            points,
            list(
                reversed(
                    radial_blend_points(
                        spec.root_radius,
                        spec.base_radius,
                        right_base_angle + tooth_angle,
                        spec.root_fillet_steps,
                        center,
                        rotation,
                        include_start=True,
                    )
                )
            ),
        )
        append_points(
            points,
            arc_points(
                spec.root_radius,
                right_base_angle + tooth_angle,
                left_base_angle + next_tooth_angle,
                spec.root_steps,
                center,
                rotation,
            ),
        )

    return points


def slot_profile_points(
    spec: SpurGearSpec,
    tooth: int,
    *,
    center: tuple[float, float] = (0.0, 0.0),
    rotation: float = 0.0,
) -> list[tuple[float, float]]:
    right = flank_points(spec, mirror=False, center=(0.0, 0.0), rotation=0.0)
    left = flank_points(spec, mirror=True, center=(0.0, 0.0), rotation=0.0)
    right_base_angle = polar(right[0])[1]
    right_tip_angle = polar(right[-1])[1]
    left_base_angle = polar(left[0])[1]
    left_tip_angle = polar(left[-1])[1]
    tooth_pitch = 2.0 * math.pi / spec.teeth
    tooth_angle = tooth * tooth_pitch
    next_tooth_angle = (tooth + 1) * tooth_pitch

    points: list[tuple[float, float]] = [
        point_at(spec.cutter_outer_radius, right_tip_angle + tooth_angle, center, rotation)
    ]
    append_points(
        points,
        arc_points(
            spec.cutter_outer_radius,
            right_tip_angle + tooth_angle,
            left_tip_angle + next_tooth_angle,
            spec.tip_steps,
            center,
            rotation,
        ),
    )
    append_points(points, transformed(list(reversed(left)), center, next_tooth_angle + rotation))
    append_points(
        points,
        list(
            reversed(
                radial_blend_points(
                    spec.root_radius,
                    spec.base_radius,
                    left_base_angle + next_tooth_angle,
                    spec.root_fillet_steps,
                    center,
                    rotation,
                    include_start=True,
                )
            )
        ),
    )
    root_arc = arc_points(
        spec.root_radius,
        right_base_angle + tooth_angle,
        left_base_angle + next_tooth_angle,
        spec.root_steps,
        center,
        rotation,
        include_start=True,
    )
    append_points(points, list(reversed(root_arc)))
    append_points(
        points,
        radial_blend_points(
            spec.root_radius,
            spec.base_radius,
            right_base_angle + tooth_angle,
            spec.root_fillet_steps,
            center,
            rotation,
        ),
    )
    append_points(points, transformed(right[1:], center, tooth_angle + rotation))
    return points


def transformed_point(point: tuple[float, float], center: tuple[float, float], rotation: float) -> tuple[float, float]:
    x, y = rotate(point, rotation)
    return x + center[0], y + center[1]


def draw_three_point_arc(
    sk,
    radius: float,
    start_angle: float,
    end_angle: float,
    center: tuple[float, float],
    rotation: float,
) -> object:
    mid_angle = 0.5 * (start_angle + end_angle)
    start = point_at(radius, start_angle, center, rotation)
    end = point_at(radius, end_angle, center, rotation)
    mid = point_at(radius, mid_angle, center, rotation)
    return sk.three_point_arc(start[0], start[1], end[0], end[1], mid[0], mid[1])


def draw_center_arc(
    sk,
    radius: float,
    start_angle: float,
    end_angle: float,
    center: tuple[float, float],
    rotation: float,
    *,
    direction: int,
) -> object:
    start = point_at(radius, start_angle, center, rotation)
    end = point_at(radius, end_angle, center, rotation)
    return sk.arc(center[0], center[1], start[0], start[1], end[0], end[1], direction=direction)


def involute_equation_expressions(base_radius: float, rotation: float, *, mirror: bool = False, parameter: str = "t") -> tuple[str, str]:
    rb = expression_mm(base_radius)
    c = expression(math.cos(rotation))
    s = expression(math.sin(rotation))
    t = f"({parameter})"
    raw_x = f"({rb})*(cos({t})+({t})*sin({t}))"
    raw_y = f"({rb})*(sin({t})-({t})*cos({t}))"
    if mirror:
        raw_y = f"-({raw_y})"
    x_expr = f"({raw_x})*({c})-({raw_y})*({s})"
    y_expr = f"({raw_x})*({s})+({raw_y})*({c})"
    return x_expr, y_expr


def draw_slot_profile(sk, spec: SpurGearSpec, tooth: int, *, rotation: float = 0.0) -> None:
    right = flank_points(spec, mirror=False, center=(0.0, 0.0), rotation=0.0)
    left = flank_points(spec, mirror=True, center=(0.0, 0.0), rotation=0.0)
    right_base_angle = polar(right[0])[1]
    right_tip_angle = polar(right[-1])[1]
    left_base_angle = polar(left[0])[1]
    left_tip_angle = polar(left[-1])[1]
    tooth_pitch = 2.0 * math.pi / spec.teeth
    tooth_angle = tooth * tooth_pitch
    next_tooth_angle = (tooth + 1) * tooth_pitch

    right_tip_outer = point_at(spec.outer_radius, right_tip_angle + tooth_angle, (0.0, 0.0), rotation)
    right_tip_cutter = point_at(spec.cutter_outer_radius, right_tip_angle + tooth_angle, (0.0, 0.0), rotation)
    left_tip_outer = point_at(spec.outer_radius, left_tip_angle + next_tooth_angle, (0.0, 0.0), rotation)
    left_tip_cutter = point_at(spec.cutter_outer_radius, left_tip_angle + next_tooth_angle, (0.0, 0.0), rotation)

    segments: list[object] = []
    segments.extend(sk.polyline([right_tip_outer, right_tip_cutter], close=False))
    segments.append(draw_center_arc(
        sk,
        spec.cutter_outer_radius,
        right_tip_angle + tooth_angle,
        left_tip_angle + next_tooth_angle,
        (0.0, 0.0),
        rotation,
        direction=1,
    ))
    segments.extend(sk.polyline([left_tip_cutter, left_tip_outer], close=False))

    base_to_outer_t = math.sqrt((spec.outer_radius / spec.base_radius) ** 2 - 1.0)
    t_max = expression(base_to_outer_t)
    left_x, left_y = involute_equation_expressions(
        spec.base_radius,
        left_base_angle + next_tooth_angle + rotation,
        parameter=f"({t_max})-t",
    )
    right_x, right_y = involute_equation_expressions(spec.base_radius, right_base_angle + tooth_angle + rotation, mirror=True)

    left_flank = sk.equation_spline(
        left_x,
        left_y,
        range_start="0",
        range_end=t_max,
        lock_start=True,
        lock_end=True,
    )
    segments.append(left_flank)

    left_base_point = point_at(spec.base_radius, left_base_angle + next_tooth_angle, (0.0, 0.0), rotation)
    left_root_point = point_at(spec.root_radius, left_base_angle + next_tooth_angle, (0.0, 0.0), rotation)
    right_root_point = point_at(spec.root_radius, right_base_angle + tooth_angle, (0.0, 0.0), rotation)
    right_base_point = point_at(spec.base_radius, right_base_angle + tooth_angle, (0.0, 0.0), rotation)

    segments.extend(sk.polyline([left_base_point, left_root_point], close=False))
    segments.append(
        draw_center_arc(
            sk,
            spec.root_radius,
            left_base_angle + next_tooth_angle,
            right_base_angle + tooth_angle,
            (0.0, 0.0),
            rotation,
            direction=-1,
        )
    )
    segments.extend(sk.polyline([right_root_point, right_base_point], close=False))

    right_flank = sk.equation_spline(
        right_x,
        right_y,
        range_start="0",
        range_end=t_max,
        lock_start=True,
        lock_end=True,
    )
    segments.append(right_flank)

    for previous, current in zip(segments, segments[1:]):
        sk.coincident_endpoints(previous, current)
    sk.coincident_endpoints(segments[-1], segments[0], b_start=True)


def draw_gear(part, spec: SpurGearSpec, rotation: float, feature_name: str) -> None:
    axis = part.insert_axis_from_planes("Front Plane", "Right Plane", name=f"{feature_name} center axis")

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        sk.circle(0.0, 0.0, spec.outer_radius)
    part.features.extrude_midplane(spec.thickness, merge=False)
    part.rename_last_feature(f"{feature_name} blank")

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        draw_slot_profile(sk, spec, 0, rotation=rotation)
        sk.select_closed_contours(min_segments=6)
    seed_cut = part.features.cut_midplane(spec.thickness * 1.5)
    seed_cut.Name = f"{feature_name} tooth space seed"

    part.clear_selection()
    part.select_object(axis, mark=1)
    part.select_object(seed_cut, append=True, mark=4)
    pattern = part.features.circular_pattern_selected(spec.teeth)
    pattern.Name = f"{feature_name} tooth space pattern"

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        sk.circle(0.0, 0.0, spec.bore_radius)
    part.features.cut_midplane(spec.thickness * 1.5)
    part.rename_last_feature(f"{feature_name} bore")


def build_gear_part(sw: SolidWorks, spec: SpurGearSpec, path: Path, *, rotation: float = 0.0) -> Path:
    part = sw.new_part()
    draw_gear(part, spec, rotation, spec.name)
    part.rebuild()
    part.save_as(path)
    return path


def build_meshing_gears(
    output_dir: Path,
    export_step: bool = True,
    visible: bool = True,
) -> tuple[Path, Path | None]:
    output_dir.mkdir(parents=True, exist_ok=True)

    gear_a = SpurGearSpec(name="driver_gear", teeth=24)
    gear_b = SpurGearSpec(name="driven_gear", teeth=36)
    center_distance = gear_a.pitch_radius + gear_b.pitch_radius

    sw = SolidWorks.connect(visible=visible)
    driver_path = build_gear_part(sw, gear_a, output_dir / "driver_24t_involute_gear.SLDPRT")
    driven_path = build_gear_part(
        sw,
        gear_b,
        output_dir / "driven_36t_involute_gear.SLDPRT",
        rotation=math.pi / gear_b.teeth,
    )

    try:
        assembly = sw.new_assembly()
    except SolidWorksError as exc:
        if export_step:
            raise
        print(f"Assembly skipped: {exc}")
        return driver_path, None

    driver = assembly.add_component(driver_path, x=0.0, y=0.0, z=0.0)
    driven = assembly.add_component(driven_path, x=center_distance, y=0.0, z=0.0)
    assembly.add_gear_mate_between_axes(
        driver,
        "driver_gear center axis",
        driven,
        "driven_gear center axis",
        numerator=gear_b.teeth,
        denominator=gear_a.teeth,
    )
    assembly.rebuild()

    sldasm_path = output_dir / "meshing_involute_gears.SLDASM"
    assembly.save_as(sldasm_path)

    step_path = None
    if export_step:
        step_path = output_dir / "meshing_involute_gears.step"
        assembly.export(step_path)

    return sldasm_path, step_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create two manufacturable meshing involute spur gears in SOLIDWORKS.")
    parser.add_argument("--output-dir", type=Path, default=Path("output") / "gears")
    parser.add_argument("--no-step", action="store_true", help="Only save the native SLDPRT file.")
    parser.add_argument("--hidden", action="store_true", help="Run SOLIDWORKS without making the window visible.")
    args = parser.parse_args()

    sldprt_path, step_path = build_meshing_gears(
        args.output_dir,
        export_step=not args.no_step,
        visible=not args.hidden,
    )
    print(f"Saved: {sldprt_path}")
    if step_path is not None:
        print(f"Exported: {step_path}")


if __name__ == "__main__":
    main()
