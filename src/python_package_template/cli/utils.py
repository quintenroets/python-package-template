import inspect
from typing import Type
from typing import Annotated
import sys
from collections.abc import Callable
from typing import Any, TypeVar

import typer


from plib import Path

T = TypeVar("T")


def create_instance_from_cli_args(
    class_type: type[T], docstring_function: Callable[..., Any] | None = None
) -> T:
    app = typer.Typer(add_completion=False)
    init = _create_init_for_cli_entry(class_type, docstring_function)
    create_command = app.command()
    create_command(init)
    init_result = app(standalone_mode=False)
    if isinstance(init_result, int):
        sys.exit(init_result)
    return init_result  # type: ignore


def _create_init_for_cli_entry(
    dataclass_type: Type[T], docstring_function: Callable[..., Any] | None
) -> Callable[[], T]:
    def cli_init(**kwargs: Any) -> T:
        return dataclass_type(**kwargs)

    if docstring_function is None:
        docstring_function = dataclass_type.__init__

    cli_init.__signature__ = _create_cli_init_signature(dataclass_type)
    cli_init.__doc__ = docstring_function.__doc__
    return cli_init


def _create_cli_init_signature(dataclass_type: Type[T]) -> inspect.Signature:
    parameters = _extract_attributes_as_parameters(dataclass_type)
    init_signature = inspect.signature(dataclass_type.__init__)
    return init_signature.replace(parameters=parameters)


def _extract_attributes_as_parameters(
    dataclass_type: type[T],
) -> list[inspect.Parameter]:
    init_signature = inspect.signature(dataclass_type.__init__)
    init_parameters = init_signature.parameters.values()
    exposed_dataclass_attributes = [
        _fix_annotation(parameter)
        for parameter in init_parameters
        if parameter.name != "self"
    ]
    return exposed_dataclass_attributes


def _fix_annotation(parameter: inspect.Parameter):
    if issubclass(parameter.annotation, Path):
        # monkey patch path convertor
        typer.main.param_path_convertor = parameter.annotation
        parameter._annotation = Annotated[
            parameter.annotation, typer.Option(path_type=parameter.annotation)
        ]
    return parameter
