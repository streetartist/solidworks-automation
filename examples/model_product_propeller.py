from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solidworks_com import SolidWorks, SolidWorksError, deg, mm


@dataclass(frozen=True)
class PropellerSpec:
    name: str = "production_5x3_two_blade_propeller"
    blade_count: int = 2
    diameter: float = mm(127.0)
    hub_radius: float = mm(15.0)
    hub_thickness: float = mm(8.0)
    bore_radius: float = mm(2.55)
    bolt_circle_radius: float = mm(6.0)
    bolt_hole_radius: float = mm(1.15)
    bolt_count: int = 4
    through_cut_depth: float = mm(24.0)


@dataclass(frozen=True)
class BladeStation:
    radius: float
    chord: float
    pitch_deg: float
    thickness_ratio: float


def naca_4digit_symmetric_surfaces(count: int = 25, thickness: float = 0.12) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    """Return upper and lower NACA 00xx airfoil surfaces from trailing edge to trailing edge."""
    upper: list[tuple[float, float]] = []
    lower: list[tuple[float, float]] = []
    for i in range(count):
        x = 0.5 * (1.0 - math.cos(math.pi * i / (count - 1)))
        yt = 5.0 * thickness * (
            0.2969 * math.sqrt(max(x, 0.0))
            - 0.1260 * x
            - 0.3516 * x**2
            + 0.2843 * x**3
            - 0.1036 * x**4
        )
        upper.append((x, yt))
        lower.append((x, -yt))
    return list(reversed(upper)), lower


def blade_stations(spec: PropellerSpec) -> list[BladeStation]:
    r_tip = spec.diameter / 2.0
    return [
        BladeStation(radius=mm(13.0), chord=mm(25.0), pitch_deg=31.0, thickness_ratio=0.145),
        BladeStation(radius=mm(21.0), chord=mm(27.0), pitch_deg=26.5, thickness_ratio=0.132),
        BladeStation(radius=mm(34.0), chord=mm(24.0), pitch_deg=20.0, thickness_ratio=0.118),
        BladeStation(radius=mm(49.0), chord=mm(18.0), pitch_deg=14.0, thickness_ratio=0.105),
        BladeStation(radius=r_tip - mm(2.0), chord=mm(7.0), pitch_deg=9.0, thickness_ratio=0.095),
        BladeStation(radius=r_tip - mm(0.15), chord=mm(0.45), pitch_deg=7.0, thickness_ratio=0.18),
    ]


def rotate_xy(x: float, y: float, angle: float) -> tuple[float, float]:
    ca = math.cos(angle)
    sa = math.sin(angle)
    return x * ca - y * sa, x * sa + y * ca


def airfoil_point(station: BladeStation, chord_x: float, thickness_z: float, blade_angle: float) -> tuple[float, float, float]:
    beta = deg(station.pitch_deg)
    chord_coord = (0.5 - chord_x) * station.chord
    airfoil_z = thickness_z * station.chord
    tangent = chord_coord * math.cos(beta) - airfoil_z * math.sin(beta)
    z = chord_coord * math.sin(beta) + airfoil_z * math.cos(beta)
    x, y = rotate_xy(station.radius, tangent, blade_angle)
    return (x, y, z)


def station_profile_curves(station: BladeStation, blade_angle: float) -> tuple[list[tuple[float, float, float]], list[tuple[float, float, float]]]:
    upper, lower = naca_4digit_symmetric_surfaces(thickness=station.thickness_ratio)
    return (
        [airfoil_point(station, x, z, blade_angle) for x, z in upper],
        [airfoil_point(station, x, z, blade_angle) for x, z in lower],
    )


def create_station_plane(part, name: str, offset_x: float) -> Any:
    part.clear_selection()
    part.select_plane("Right Plane")
    plane = part.features.offset_plane(abs(offset_x), flip=offset_x < 0.0)
    plane.Name = name
    return plane


def right_plane_sketch_points(points: list[tuple[float, float, float]]) -> list[tuple[float, float, float]]:
    return [(y, z, 0.0) for _, y, z in points]


def create_closed_profile_on_plane(
    part,
    plane: Any,
    name: str,
    upper_points: list[tuple[float, float, float]],
    lower_points: list[tuple[float, float, float]],
) -> Any:
    part.clear_selection()
    part.select_object(plane)
    with part.sketch() as sk:
        sk.spline(right_plane_sketch_points(upper_points))
        sk.spline(right_plane_sketch_points(lower_points))
    return part.rename_last_feature(name)


def loft_blade(part, sketches: list[Any], feature_name: str) -> None:
    part.clear_selection()
    for index, sketch in enumerate(sketches):
        part.select_object(sketch, append=index > 0, mark=1)
    part.features.loft_boss(
        closed=False,
        keep_tangency=False,
        force_non_rational=False,
        tess_tolerance_factor=1.2,
        start_matching_type=0,
        end_matching_type=0,
        merge=True,
    )
    part.rename_last_feature(feature_name)


def make_hub(part, spec: PropellerSpec) -> None:
    part.select_plane("Top Plane")
    with part.sketch() as sk:
        sk.circle(0.0, 0.0, spec.hub_radius)
    part.features.extrude_midplane(spec.hub_thickness)
    part.rename_last_feature("Hub")


def cut_mounting_holes(part, spec: PropellerSpec) -> None:
    part.select_plane("Top Plane")
    with part.sketch() as sk:
        sk.circle(0.0, 0.0, spec.bore_radius)
        for index in range(spec.bolt_count):
            angle = 2.0 * math.pi * index / spec.bolt_count + math.pi / 4.0
            x = spec.bolt_circle_radius * math.cos(angle)
            y = spec.bolt_circle_radius * math.sin(angle)
            sk.circle(x, y, spec.bolt_hole_radius)
    part.features.cut_midplane(spec.through_cut_depth)
    part.rename_last_feature("Shaft and mounting holes")


def add_balance_ring(part, spec: PropellerSpec) -> None:
    part.select_plane("Top Plane")
    with part.sketch() as sk:
        sk.circle(0.0, 0.0, spec.hub_radius * 0.78)
        sk.circle(0.0, 0.0, spec.hub_radius * 0.48)
    part.features.extrude_midplane(mm(1.8), merge=True)
    part.rename_last_feature("Raised balance ring")


def apply_appearance(part) -> None:
    # SOLIDWORKS uses RGB plus shininess/transparency-style material slots.
    part.com.MaterialPropertyValues = [0.04, 0.045, 0.05, 1.0, 0.55, 0.25, 0.0, 0.0, 0.0]


def build_propeller(output_dir: Path, export_step: bool = True, visible: bool = True) -> tuple[Path, Path | None]:
    spec = PropellerSpec()
    output_dir.mkdir(parents=True, exist_ok=True)

    sw = SolidWorks.connect(visible=visible)
    part = sw.new_part()

    make_hub(part, spec)
    for blade_index in range(spec.blade_count):
        angle = 2.0 * math.pi * blade_index / spec.blade_count
        if not math.isclose(math.sin(angle), 0.0, abs_tol=1e-9):
            raise SolidWorksError("This product propeller script currently supports two opposed blades.")
        profiles: list[tuple[list[tuple[float, float, float]], list[tuple[float, float, float]]]] = [
            station_profile_curves(station, angle)
            for station in blade_stations(spec)
        ]
        stations = blade_stations(spec)
        direction = 1.0 if math.cos(angle) >= 0.0 else -1.0
        planes = [
            create_station_plane(part, f"Blade {blade_index + 1} plane {station_index + 1}", direction * station.radius)
            for station_index, station in enumerate(stations)
        ]
        sketches = [
            create_closed_profile_on_plane(
                part,
                planes[station_index],
                f"Blade {blade_index + 1} station {station_index + 1}",
                profile[0],
                profile[1],
            )
            for station_index, profile in enumerate(profiles)
        ]
        loft_blade(part, sketches, f"Blade {blade_index + 1} twisted airfoil")

    add_balance_ring(part, spec)
    cut_mounting_holes(part, spec)
    # apply_appearance(part)
    part.rebuild()

    sldprt_path = output_dir / f"{spec.name}.SLDPRT"
    part.save_as(sldprt_path)

    step_path = None
    if export_step:
        step_path = output_dir / f"{spec.name}.step"
        part.export(step_path)

    return sldprt_path, step_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a manufacturable twisted two-blade propeller in SOLIDWORKS.")
    parser.add_argument("--output-dir", type=Path, default=Path("output") / "propeller")
    parser.add_argument("--no-step", action="store_true", help="Only save the native SLDPRT file.")
    parser.add_argument("--hidden", action="store_true", help="Run SOLIDWORKS without making the window visible.")
    args = parser.parse_args()

    sldprt_path, step_path = build_propeller(args.output_dir, export_step=not args.no_step, visible=not args.hidden)
    print(f"Saved: {sldprt_path}")
    if step_path is not None:
        print(f"Exported: {step_path}")


if __name__ == "__main__":
    main()
