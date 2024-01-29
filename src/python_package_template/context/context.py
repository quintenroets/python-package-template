from package_utils.context import Context, Models

from ..models import Config, Options, Secrets

models = Models(Options, Config, Secrets)
context = Context(models)
