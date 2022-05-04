from __future__ import annotations
from dataclasses import dataclass
import json
import prettytable as pt
from tables.domain import models
from tables.domain.errors import PrintersErrors
from tables.persistence.json_encoder import CustomJSONEncoder

PRETTY_TABLE_ALIGN_LEFT = 'l'

def print_dataclasses(dataclasses: list[dataclass]) -> pt.PrettyTable:
    """Create a PrettyTable of the specified list of dataclasses."""

    # do some validation on the argument
    if not dataclasses:
        raise PrintersErrors.PRINT_OBJECTS_ARG_NULL
    elif not isinstance(dataclasses, list):
        raise PrintersErrors.PRINT_OBJECTS_ARG_NOT_LIST

    # creat a new PrettyTable object with the argument's field names
    field_names = list(dataclasses[0].__dict__.keys())
    prettytable = pt.PrettyTable(field_names)

    # configure the looks of the table
    _configure_prettytable(prettytable)

    # add all the database connection rows to the table
    rows = _get_dataclasses_rows(dataclasses)
    prettytable.add_rows(rows)

    return prettytable

def _get_dataclasses_rows(dataclasses: list[dataclass]) -> list:
    """Get a list of all the values in the specified list of dataclasses"""

    rows = [list(data_class.__dict__.values()) for data_class in dataclasses]
    return rows



def get_basic_dict_list(objects: list[dict]) -> pt.PrettyTable:
    rows = [list(d.values()) for d in objects]
    prettytable = pt.PrettyTable()

    try:
        prettytable.field_names = list(objects[0].keys())
    except:
        pass

    _configure_prettytable(prettytable)
    prettytable.add_rows(rows)
    return prettytable




def _configure_prettytable(prettytable: pt.PrettyTable):
    """Modify the look of the given PrettyTable"""

    # alignment
    prettytable.align = PRETTY_TABLE_ALIGN_LEFT

    # border/overall look
    # prettytable.set_style(pt.SINGLE_BORDER)
    # prettytable.set_style(pt.MSWORD_FRIENDLY)
    # prettytable.set_style(pt.MARKDOWN)
    # prettytable.set_style(pt.DOUBLE_BORDER)
    # prettytable.set_style(pt.PLAIN_COLUMNS)
    # prettytable.set_style(pt.ORGMODE)



def dump_json(data):
    return json.dumps(data, indent=4, cls=CustomJSONEncoder)
    
