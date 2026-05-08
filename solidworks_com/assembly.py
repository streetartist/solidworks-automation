from __future__ import annotations

from pathlib import Path
from typing import Any

from .com import call_member, int_byref
from .constants import AddComponentConfigOptions, AddMateError, MateAlign, MateType
from .errors import SolidWorksError
from .model import ModelDoc


class Component:
    def __init__(self, com: Any) -> None:
        self.com = com

    @property
    def name(self) -> str:
        return str(self.com.Name2)

    def select(self, append: bool = False, mark: int = 0) -> bool:
        return bool(call_member(self.com, "Select4", bool(append), None, int(mark), default=False))


class AssemblyDoc(ModelDoc):
    @property
    def assembly(self) -> Any:
        return self.com

    def add_component(
        self,
        path: str | Path,
        *,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
        config_option: int | AddComponentConfigOptions = AddComponentConfigOptions.CurrentSelectedConfig,
        existing_config: str = "",
        new_config: str = "",
        use_config_for_part_references: bool = False,
    ) -> Component:
        path = Path(path).resolve()
        component = self.assembly.AddComponent5(
            str(path),
            int(config_option),
            new_config,
            bool(use_config_for_part_references),
            existing_config,
            float(x),
            float(y),
            float(z),
        )
        if component is None:
            raise SolidWorksError(f"Failed to add assembly component: {path}")
        return Component(component)

    def add_components(self, *paths: str | Path, spacing: float = 0.0) -> list[Component]:
        components: list[Component] = []
        for index, path in enumerate(paths):
            components.append(self.add_component(path, x=index * spacing))
        return components

    def select_component_feature(
        self,
        component: Component,
        feature_name: str,
        object_type: str,
        *,
        append: bool = False,
        mark: int = 0,
        require: bool = True,
    ) -> bool:
        candidates = [
            f"{feature_name}@{component.name}",
            f"{feature_name}@{component.name}@{self.title}",
            f"{feature_name}@{component.name.split('/')[0]}",
            f"{feature_name}@{component.name.split('/')[0]}@{self.title}",
        ]
        for name in candidates:
            if self.select_by_id(name, object_type, append=append, mark=mark, require=False):
                return True
        if require:
            raise SolidWorksError(f"Failed to select {object_type}: {feature_name} in {component.name}")
        return False

    def add_mate_selected(
        self,
        mate_type: int | MateType,
        *,
        align: int | MateAlign = MateAlign.Closest,
        flip: bool = False,
        distance: float = 0.0,
        gear_ratio_numerator: float = 0.0,
        gear_ratio_denominator: float = 0.0,
        angle: float = 0.0,
        for_positioning_only: bool = False,
        lock_rotation: bool = False,
        width_mate_option: int = 0,
    ) -> Any:
        error = int_byref()
        try:
            mate = self.assembly.AddMate5(
                int(mate_type),
                int(align),
                bool(flip),
                float(distance),
                0.0,
                0.0,
                float(gear_ratio_numerator),
                float(gear_ratio_denominator),
                float(angle),
                0.0,
                0.0,
                bool(for_positioning_only),
                bool(lock_rotation),
                int(width_mate_option),
                error,
            )
            err = int(getattr(error, "value", 0) or 0)
        except TypeError:
            result = self.assembly.AddMate5(
                int(mate_type),
                int(align),
                bool(flip),
                float(distance),
                0.0,
                0.0,
                float(gear_ratio_numerator),
                float(gear_ratio_denominator),
                float(angle),
                0.0,
                0.0,
                bool(for_positioning_only),
                bool(lock_rotation),
                int(width_mate_option),
                0,
            )
            mate = result[0] if isinstance(result, tuple) else result
            err = int(result[-1]) if isinstance(result, tuple) and result else 0
        if mate is None or err not in (0, int(AddMateError.NoError)):
            raise SolidWorksError(f"Failed to add mate type {int(mate_type)}", errors=err)
        return mate

    def add_gear_mate_selected(
        self,
        numerator: float,
        denominator: float,
        *,
        align: int | MateAlign = MateAlign.Closest,
    ) -> Any:
        return self.add_mate_selected(
            MateType.Gear,
            align=align,
            gear_ratio_numerator=numerator,
            gear_ratio_denominator=denominator,
        )

    def add_coincident_mate_selected(
        self,
        *,
        align: int | MateAlign = MateAlign.Closest,
    ) -> Any:
        return self.add_mate_selected(MateType.Coincident, align=align)

    def add_concentric_mate_selected(
        self,
        *,
        align: int | MateAlign = MateAlign.Closest,
        lock_rotation: bool = False,
    ) -> Any:
        return self.add_mate_selected(MateType.Concentric, align=align, lock_rotation=lock_rotation)

    def add_parallel_mate_selected(
        self,
        *,
        align: int | MateAlign = MateAlign.Closest,
    ) -> Any:
        return self.add_mate_selected(MateType.Parallel, align=align)

    def add_tangent_mate_selected(
        self,
        *,
        align: int | MateAlign = MateAlign.Closest,
    ) -> Any:
        return self.add_mate_selected(MateType.Tangent, align=align)

    def add_distance_mate_selected(
        self,
        distance: float,
        *,
        align: int | MateAlign = MateAlign.Closest,
        flip: bool = False,
    ) -> Any:
        return self.add_mate_selected(MateType.Distance, align=align, flip=flip, distance=distance)

    def select_face_for_mate_by_ray(
        self,
        origin: tuple[float, float, float],
        direction: tuple[float, float, float],
        *,
        radius: float,
        append: bool = False,
        mark: int = 1,
        require: bool = True,
    ) -> bool:
        return self.select_face_by_ray(origin, direction, radius=radius, append=append, mark=mark, require=require)

    def select_edge_for_mate_by_ray(
        self,
        origin: tuple[float, float, float],
        direction: tuple[float, float, float],
        *,
        radius: float,
        append: bool = False,
        mark: int = 1,
        require: bool = True,
    ) -> bool:
        return self.select_edge_by_ray(origin, direction, radius=radius, append=append, mark=mark, require=require)

    def add_tangent_mate_between_ray_faces(
        self,
        first_origin: tuple[float, float, float],
        first_direction: tuple[float, float, float],
        second_origin: tuple[float, float, float],
        second_direction: tuple[float, float, float],
        *,
        radius: float,
        align: int | MateAlign = MateAlign.Closest,
    ) -> Any:
        self.clear_selection()
        self.select_face_for_mate_by_ray(first_origin, first_direction, radius=radius)
        self.select_face_for_mate_by_ray(second_origin, second_direction, radius=radius, append=True)
        return self.add_tangent_mate_selected(align=align)

    def add_coincident_mate_between_ray_faces(
        self,
        first_origin: tuple[float, float, float],
        first_direction: tuple[float, float, float],
        second_origin: tuple[float, float, float],
        second_direction: tuple[float, float, float],
        *,
        radius: float,
        align: int | MateAlign = MateAlign.Closest,
    ) -> Any:
        self.clear_selection()
        self.select_face_for_mate_by_ray(first_origin, first_direction, radius=radius)
        self.select_face_for_mate_by_ray(second_origin, second_direction, radius=radius, append=True)
        return self.add_coincident_mate_selected(align=align)

    def add_gear_mate_between_axes(
        self,
        component_a: Component,
        axis_a: str,
        component_b: Component,
        axis_b: str,
        *,
        numerator: float,
        denominator: float,
        align: int | MateAlign = MateAlign.Closest,
    ) -> Any:
        self.clear_selection()
        self.select_component_feature(component_a, axis_a, "AXIS")
        self.select_component_feature(component_b, axis_b, "AXIS", append=True)
        return self.add_gear_mate_selected(numerator, denominator, align=align)
