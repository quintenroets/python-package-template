import cli

from python_package_template.context import context


def main() -> None:
    """
    Python package template.
    """
    message = "main functionality"
    if context.options.debug:
        cli.console.print(message)
    cli.console.print(context.secrets)
