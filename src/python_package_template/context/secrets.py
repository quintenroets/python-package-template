from dataclasses import dataclass

@dataclass
class SubSecrets:
    token: str

@dataclass
class Secrets:
    # token: str
    sub: SubSecrets
