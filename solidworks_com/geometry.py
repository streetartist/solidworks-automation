from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Point:
    x: float
    y: float
    z: float = 0.0

    def as_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)


@dataclass(frozen=True)
class Vector:
    x: float
    y: float
    z: float = 0.0

    def as_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)


def flatten_points(points: Iterable[Point | tuple[float, float] | tuple[float, float, float]]) -> list[float]:
    data: list[float] = []
    for point in points:
        if isinstance(point, Point):
            data.extend(point.as_tuple())
        elif len(point) == 2:
            data.extend((float(point[0]), float(point[1]), 0.0))
        else:
            data.extend((float(point[0]), float(point[1]), float(point[2])))
    return data
