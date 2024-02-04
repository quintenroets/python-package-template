from __future__ import annotations

import plib
from simple_classproperty import classproperty


class Path(plib.Path):
    @classproperty
    def source_root(cls) -> Path:
        return cls(__file__).parent.parent  # type: ignore

    @classproperty
    def assets(cls) -> Path:
        return cls.script_assets / cls.source_root.name  # type: ignore

    @classproperty
    def config(cls) -> Path:
        return cls.assets / "config" / "config.yaml"  # type: ignore
