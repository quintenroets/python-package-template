from __future__ import annotations

from collections.abc import Callable

import plib
from simple_classproperty import classproperty as untyped_classproperty


classproperty: Callable[[Callable[[Path], Path]], Path] = untyped_classproperty  # noqa


class Path(plib.Path):  # type: ignore
    @classproperty
    def root(cls: type[Path]) -> Path:
        return cls(__file__).parent.parent  # type: ignore

    @classproperty
    def assets(cls: type[Path]) -> Path:
        return cls.script_assets / cls.root.name  # type: ignore

    @classproperty
    def config(cls: type[Path]) -> Path:
        return cls.assets / "config" / "config.yaml"  # type: ignore
