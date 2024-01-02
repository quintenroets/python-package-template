from python_package_template import main

from ..context import context
from ..context.options import Options
from .utils import create_instance_from_cli_args


def entry_point() -> None:
    context.options = create_instance_from_cli_args(Options, docstring_function=main)
    main()


if __name__ == "__main__":
    entry_point()
