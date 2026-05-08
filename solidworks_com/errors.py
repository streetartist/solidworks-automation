from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ApiResult:
    ok: bool
    errors: int = 0
    warnings: int = 0


class SolidWorksError(RuntimeError):
    def __init__(self, message: str, *, errors: int = 0, warnings: int = 0) -> None:
        super().__init__(message)
        self.errors = errors
        self.warnings = warnings

    def __str__(self) -> str:
        details = []
        if self.errors:
            details.append(f"errors={self.errors}")
        if self.warnings:
            details.append(f"warnings={self.warnings}")
        if not details:
            return super().__str__()
        return f"{super().__str__()} ({', '.join(details)})"
