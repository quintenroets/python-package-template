import pytest
from python_package_template import cli


@pytest.mark.skip()
def test_testing() -> None:
    cli.entry_point()
