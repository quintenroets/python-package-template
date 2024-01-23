from package_dev_utils.tests.args import no_cli_args
from python_package_template import cli


@no_cli_args
def test_testing() -> None:
    cli.entry_point()
