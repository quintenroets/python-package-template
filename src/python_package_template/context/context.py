from package_utils.context import Context

from .config import Config
from .options import Options
from .secrets_ import Secrets

context = Context(Options, Config, Secrets)
