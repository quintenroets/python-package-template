from __future__ import annotations

import plib
from simple_classproperty import classproperty


class Path(plib.Path):  # type: ignore
    @classproperty
    def source_root(cls: type[Path]) -> Path:
        return cls(__file__).parent.parent  # type: ignore

    @classproperty
    def assets(cls: type[Path]) -> Path:
        return cls.script_assets / cls.source_root.name  # type: ignore

    @classproperty
    def config(cls: type[Path]) -> Path:
        return cls.assets / "config" / "config.yaml"  # type: ignore
