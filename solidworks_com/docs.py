from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class EnumMember:
    name: str
    value: int | None
    description: str


_MEMBER_RE = re.compile(r"^\|\s*\*\*(?P<name>[^*]+)\*\*\s*\|\s*(?P<desc>.*?)\s*\|$")
_NUMBER_RE = re.compile(r"(?<![A-Za-z_])(?:-?\d+|0x[0-9A-Fa-f]+)")


def parse_enum_markdown(path: str | Path) -> dict[str, EnumMember]:
    """Parse one SOLIDWORKS enum markdown file from scripts/docs/swconst."""
    members: dict[str, EnumMember] = {}
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        match = _MEMBER_RE.match(line)
        if not match:
            continue
        name = match.group("name").replace("\\_", "_")
        desc = match.group("desc").replace("\\_", "_")
        number = _NUMBER_RE.search(desc)
        value = int(number.group(0), 0) if number else None
        members[name] = EnumMember(name=name, value=value, description=desc)
    return members


def load_swconst_docs(root: str | Path) -> dict[str, dict[str, EnumMember]]:
    """Load all enum markdown files under a converted SOLIDWORKS swconst docs folder."""
    root = Path(root)
    enums: dict[str, dict[str, EnumMember]] = {}
    for path in root.glob("SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.*_e.md"):
        enum_name = path.stem.rsplit(".", 1)[-1]
        enums[enum_name] = parse_enum_markdown(path)
    return enums
