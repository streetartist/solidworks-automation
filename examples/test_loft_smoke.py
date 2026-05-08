from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solidworks_com import SolidWorks, mm


def make_offset_plane(part, name: str, distance: float):
    part.clear_selection()
    part.select_plane("Right Plane")
    plane = part.features.offset_plane(distance)
    plane.Name = name
    return plane


def make_rectangle_profile(part, plane, name: str, half_width: float, half_height: float):
    part.clear_selection()
    part.select_object(plane)
    with part.sketch() as sk:
        sk.polyline(
            [
                (-half_width, -half_height, 0.0),
                (half_width, -half_height, 0.0),
                (half_width, half_height, 0.0),
                (-half_width, half_height, 0.0),
            ],
            close=True,
        )
    return part.rename_last_feature(name)


def main() -> None:
    sw = SolidWorks.connect(visible=True)
    part = sw.new_part()

    plane1 = make_offset_plane(part, "Loft smoke plane 1", mm(20))
    plane2 = make_offset_plane(part, "Loft smoke plane 2", mm(45))
    sketch1 = make_rectangle_profile(part, plane1, "Loft smoke profile 1", mm(6), mm(2))
    sketch2 = make_rectangle_profile(part, plane2, "Loft smoke profile 2", mm(3), mm(1))

    part.clear_selection()
    part.select_object(sketch1, mark=1)
    part.select_object(sketch2, append=True, mark=1)
    part.features.loft_boss(keep_tangency=False)
    part.rename_last_feature("Loft smoke boss")
    part.rebuild()

    out = Path("output") / "loft_smoke.SLDPRT"
    out.parent.mkdir(parents=True, exist_ok=True)
    part.save_as(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
