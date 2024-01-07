from ..context import context


def main() -> None:
    """
    This is the docstring.
    """
    message = "main functionality"
    if context.options.debug:
        print(message)
    print(context.secrets)
