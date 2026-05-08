from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from model_meshing_gears import SpurGearSpec, draw_slot_profile
from solidworks_com import SolidWorks


def build_equation_slot_profile_test(output_dir: Path, visible: bool = True) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    sw = SolidWorks.connect(visible=visible)
    part = sw.new_part()
    spec = SpurGearSpec(name="slot_profile_debug", teeth=24)

    part.select_plane("Top Plane")
    with part.sketch() as sk:
        sk.circle(0.0, 0.0, spec.root_radius)
        sk.circle(0.0, 0.0, spec.base_radius)
        sk.circle(0.0, 0.0, spec.outer_radius)
        sk.circle(0.0, 0.0, spec.cutter_outer_radius)
        draw_slot_profile(sk, spec, 0)

    part.rebuild()
    path = output_dir / "equation_slot_profile_debug.SLDPRT"
    part.save_as(path)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a single equation-driven gear slot sketch for debugging.")
    parser.add_argument("--output-dir", type=Path, default=Path("output") / "gears_equation")
    parser.add_argument("--hidden", action="store_true", help="Run SOLIDWORKS without making the window visible.")
    args = parser.parse_args()

    path = build_equation_slot_profile_test(args.output_dir, visible=not args.hidden)
    print(f"Saved: {path}")


if __name__ == "__main__":
    main()
