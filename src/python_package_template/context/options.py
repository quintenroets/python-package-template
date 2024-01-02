from dataclasses import dataclass


from ..models import Path


@dataclass
class Options:
    debug: bool = False
    config_path: Path = Path.config
