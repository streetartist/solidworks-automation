from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solidworks_com import SolidWorks, mm


def build_contour_selection_test(output_dir: Path, visible: bool = True) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    sw = SolidWorks.connect(visible=visible)
    part = sw.new_part()

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        sk.circle(0.0, 0.0, mm(40))
    part.features.extrude_midplane(mm(8))

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        lines = sk.polyline(
            [
                (-mm(10), -mm(6), 0.0),
                (mm(10), -mm(6), 0.0),
                (mm(10), mm(6), 0.0),
                (-mm(10), mm(6), 0.0),
            ]
        )
        sk.coincident_endpoints(lines[-1], lines[0])
        contours = sk.select_closed_contours(min_segments=4)
        if len(contours) != 1:
            raise RuntimeError(f"Expected one closed contour, got {len(contours)}")
    part.features.cut_midplane(mm(12))

    path = output_dir / "contour_selection_cut_test.SLDPRT"
    part.save_as(path)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Smoke-test sketch relations and contour selection.")
    parser.add_argument("--output-dir", type=Path, default=Path("output") / "contour_selection")
    parser.add_argument("--hidden", action="store_true", help="Run SOLIDWORKS without making the window visible.")
    args = parser.parse_args()

    path = build_contour_selection_test(args.output_dir, visible=not args.hidden)
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()
