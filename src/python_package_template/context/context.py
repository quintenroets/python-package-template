from package_utils.context import Context

from python_package_template.models import Config, Options, Secrets

context = Context(Options, Config, Secrets)
