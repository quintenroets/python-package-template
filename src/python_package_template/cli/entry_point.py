from package_utils.context.entry_point import create_entry_point

from python_package_template import main

from ..context import context

entry_point = create_entry_point(main, context)
