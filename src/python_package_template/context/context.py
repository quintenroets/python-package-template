from dataclasses import dataclass
from typing import TypeVar

import dacite
from plib import Path

from .config import Config
from .options import Options
from .secrets import Secrets

T = TypeVar("T")


@dataclass
class Context:
    _options: Options | None = None
    _config: Config | None = None
    _secrets: Secrets | None = None

    @property
    def options(self) -> Options:
        if self._options is None:
            self._options = Options()
        return self._options

    @options.setter
    def options(self, options: Options) -> None:
        self._options = options

    @property
    def config(self) -> Config:
        if self._config is None:
            self._config = self.read_config_from_file()
        return self._config

    @property
    def secrets(self) -> Secrets:
        if self._secrets is None:
            self._secrets = self.load_secrets()
        return self._secrets

    @classmethod
    def load_from_file(cls, class_type: type[T], path: Path) -> T:
        return dacite.from_dict(class_type, path.yaml)  # type: ignore

    def read_config_from_file(self) -> Config:
        return self.load_from_file(Config, self.options.config_path)

    def load_secrets(self) -> Secrets:
        type_hooks = {str: self.check_empty}
        secrets_dict = (
            {} if self.config.secrets_path is None else self.config.secrets_path.yaml
        )
        config = dacite.Config(type_hooks=type_hooks)
        return dacite.from_dict(Secrets, secrets_dict, config)  # type: ignore

    def check_empty(self, value: str) -> str:
        print("HIER")
        print(value)
        exit()
        return value
