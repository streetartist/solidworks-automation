from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solidworks_com import SolidWorks, mm


def build_minimal_equation_spline_test(output_dir: Path, visible: bool = True) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    sw = SolidWorks.connect(visible=visible)
    part = sw.new_part()

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        # Official SOLIDWORKS API Help style sanity checks for CreateEquationSpline2.
        sk.equation_spline(
            "t*sin(t)",
            "t*cos(t)",
            range_start="0",
            range_end="4*pi",
        )
        sk.equation_spline(
            "sin(t)",
            "cos(t)",
            range_start="0",
            range_end="pi",
            x_offset=15.0,
        )
        sk.equation_spline(
            "",
            "x^2",
            range_start="-5",
            range_end="5",
            x_offset=30.0,
        )

    part.rebuild()
    path = output_dir / "equation_spline_official_test.SLDPRT"
    part.save_as(path)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create minimal equation-driven spline sanity checks in SOLIDWORKS.")
    parser.add_argument("--output-dir", type=Path, default=Path("output") / "gears")
    parser.add_argument("--hidden", action="store_true", help="Run SOLIDWORKS without making the window visible.")
    args = parser.parse_args()

    path = build_minimal_equation_spline_test(args.output_dir, visible=not args.hidden)
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()
