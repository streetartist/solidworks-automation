from __future__ import annotations

from pathlib import Path
from typing import Any

from .app import SolidWorks
from .model import ModelDoc


class PartBuilder:
    """Convenience layer for script-generated parts.

    Methods return ``self`` where possible so larger generators can read like a
    modeling recipe while still allowing access to ``part.com`` for raw API use.
    """

    def __init__(self, part: ModelDoc) -> None:
        self.part = part

    @classmethod
    def new(cls, sw: SolidWorks) -> "PartBuilder":
        return cls(sw.new_part())

    def box(self, width: float, depth: float, height: float, *, plane: str = "Top Plane") -> "PartBuilder":
        self.part.select_plane(plane)
        with self.part.sketch() as sk:
            sk.center_rectangle(0.0, 0.0, width / 2.0, depth / 2.0)
        self.part.features.extrude_blind(height)
        return self

    def cylinder(self, radius: float, height: float, *, plane: str = "Top Plane") -> "PartBuilder":
        self.part.select_plane(plane)
        with self.part.sketch() as sk:
            sk.circle(0.0, 0.0, radius)
        self.part.features.extrude_blind(height)
        return self

    def save_as(self, path: str | Path) -> "PartBuilder":
        self.part.save_as(path)
        return self

    @property
    def com(self) -> Any:
        return self.part.com
