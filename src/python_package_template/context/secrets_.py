import os
from dataclasses import dataclass, field


@dataclass
class ApiSecrets:
    token: str = field(default_factory=lambda: os.environ.get("API_TOKEN", ""))


@dataclass
class Secrets:
    api: ApiSecrets
