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
class InvoluteSpec:
    teeth: int = 8
    module: float = mm(5.0)
    pressure_angle: float = math.radians(20.0)

    @property
    def pitch_radius(self) -> float:
        return 0.5 * self.module * self.teeth

    @property
    def base_radius(self) -> float:
        return self.pitch_radius * math.cos(self.pressure_angle)

    @property
    def outer_radius(self) -> float:
        return self.pitch_radius + self.module


def expr(value: float) -> str:
    return f"{value:.12g}"


def expr_mm(value: float) -> str:
    return f"{value * 1000.0:.12g}"


def build_single_involute_test(output_dir: Path, visible: bool = True) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    spec = InvoluteSpec()
    sw = SolidWorks.connect(visible=visible)
    part = sw.new_part()

    # SOLIDWORKS COM geometry uses meters, but equation-driven curve
    # expressions are evaluated in the document length unit in typical part
    # templates. The default templates in this repo are millimeter-based.
    rb = expr_mm(spec.base_radius)
    t_end = math.sqrt((spec.outer_radius / spec.base_radius) ** 2 - 1.0)

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        sk.circle(0.0, 0.0, spec.base_radius)
        sk.circle(0.0, 0.0, spec.outer_radius)
        sk.equation_spline(
            f"({rb})*(cos(t)+t*sin(t))",
            f"({rb})*(sin(t)-t*cos(t))",
            range_start="0",
            range_end=expr(t_end),
            lock_start=True,
            lock_end=True,
        )

    part.rebuild()
    path = output_dir / "equation_single_involute_test_mm_expr.SLDPRT"
    part.save_as(path)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create one raw equation-driven involute curve in SOLIDWORKS.")
    parser.add_argument("--output-dir", type=Path, default=Path("output") / "gears")
    parser.add_argument("--hidden", action="store_true", help="Run SOLIDWORKS without making the window visible.")
    args = parser.parse_args()

    path = build_single_involute_test(args.output_dir, visible=not args.hidden)
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()
