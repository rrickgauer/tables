from __future__ import annotations
from dataclasses import dataclass
import json
import prettytable as pt
from tables.domain import models
from tables.errors import PrintersErrors
from tables.json_encoder import CustomJSONEncoder

PRETTY_TABLE_ALIGN_LEFT = 'l'

def get_database_connections(database_connections: list[models.DatabaseConnection]) -> str:
    """Get a prettified table form of the specified database connections."""

    # do some validation on the argument
    if not database_connections:
        raise PrintersErrors.PRINT_OBJECTS_ARG_NULL
    elif not isinstance(database_connections, list):
        raise PrintersErrors.PRINT_OBJECTS_ARG_NOT_LIST

    # creat a new PrettyTable object with the argument's field names
    field_names = list(database_connections[0].__dict__.keys())
    prettytable = pt.PrettyTable(field_names)

    # configure the looks of the table
    _configure_prettytable(prettytable)

    # add all the database connection rows to the table
    rows = _get_dataclasses_rows(database_connections)
    prettytable.add_rows(rows)

    return prettytable
    
    

def _get_dataclasses_rows(dataclasses: list[dataclass]) -> list:
    """Get a list of all the values in the specified list of dataclasses"""

    rows = [list(data_class.__dict__.values()) for data_class in dataclasses]
    return rows


def _configure_prettytable(prettytable: pt.PrettyTable):
    """Modify the look of the given PrettyTable"""

    # alignment
    prettytable.align = PRETTY_TABLE_ALIGN_LEFT

    # border/overall look
    prettytable.set_style(pt.SINGLE_BORDER)
    # prettytable.set_style(pt.MSWORD_FRIENDLY)
    # prettytable.set_style(pt.MARKDOWN)
    # prettytable.set_style(pt.DOUBLE_BORDER)
    # prettytable.set_style(pt.PLAIN_COLUMNS)
    # prettytable.set_style(pt.ORGMODE)



def dump_json(data):
    return json.dumps(data, indent=4, cls=CustomJSONEncoder)
    
