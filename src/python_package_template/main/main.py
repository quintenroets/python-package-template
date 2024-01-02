from ..context import context


def main() -> None:
    """
    This is the docstring.
    """
    message = "main functionality"
    if context.options.debug:
        print(message)
    print(context.options.config_path)
    print(context.options.config_path.config)
    return
    print(context.options.config_path.name)
    print(context.secrets)
    if context.options.config_path is not None:
        print(context.options.config_path)
