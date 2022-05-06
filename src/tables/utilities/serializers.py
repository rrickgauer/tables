from __future__ import annotations
from dataclasses import dataclass
from tables.cli.choices import VIEW_COLUMN_CHOICES_DEFAULT
from tables.domain import models, views, enums, constants
from datetime import datetime

def to_database_connection(data: dict) -> models.DatabaseConnection:
    """Serialize the given dictionary into a DatabaseConnection object."""
    database_connection = serialize_dataclass(data, models.DatabaseConnection)

    try:
        database_connection.created_on = datetime.fromisoformat(database_connection.created_on)
    except (ValueError, TypeError):
        pass

    return database_connection


def to_sql_database_tables_list_view(data: dict) -> views.SqlTableTypeView:
    """Serialize the specified dictionary into a SqlTableTypeView object."""
    
    table_type = views.SqlTableTypeView(
        table_name = data.get('table_name') or None,
        table_type = data.get('table_type') or None,
    )

    if table_type.table_type:
        table_type.table_type = enums.SqlTableType(table_type.table_type)
    
    return table_type


def serialize_view_command_cli_arg_flags(data: dict) -> models.ViewCommandCliArgFlags:
    """Serialize the dictionary into a ViewCommandCliArgFlags object."""

    model = serialize_dataclass(data, models.ViewCommandCliArgFlags)

    try:
        model.format = enums.ViewCommandOutputFormat(model.format)
    except:
        model.format = enums.ViewCommandOutputFormat.TABLE

    if model.columns is None:
        model.columns = VIEW_COLUMN_CHOICES_DEFAULT

    return model


def serialize_dataclass(data: dict, model_class: dataclass):
    """Create an instance of the specified dataclass with values from the given dictionary."""

    # get a list of all the Model's attributes
    model = model_class()
    model_keys = list(model.__annotations__.keys())

    # if the dict's key is an attribute in the model, copy over the value
    for key, value in data.items():
        if not key in model_keys:
            continue

        # if value is not None:
        setattr(model, key, value)
        
        # setattr(model, key, value or None)

    decode_attribute_values(model)

    return model


def decode_attribute_values(model: dataclass):
    """Decode the specified model's attributes that are bytes."""

    for key, value in model.__dict__.items():
        if not isinstance(value, bytes):
            continue
    
        try:
            decoded_value = value.decode(constants.SQL_DATA_ENCODING)
            setattr(model, key, decoded_value)
        except:
            pass