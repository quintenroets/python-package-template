from dataclasses import dataclass

from python_package_template.models.path import Path


@dataclass
class Options:
    debug: bool = True
    config_path: Path = Path.config
