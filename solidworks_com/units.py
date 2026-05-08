from __future__ import annotations

import math


def mm(value: float) -> float:
    return value / 1000.0


def cm(value: float) -> float:
    return value / 100.0


def inch(value: float) -> float:
    return value * 0.0254


def deg(value: float) -> float:
    return math.radians(value)
