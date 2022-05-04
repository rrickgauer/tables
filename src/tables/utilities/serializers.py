from __future__ import annotations
from tables.domain import models, views, enums
from datetime import datetime


def to_database_connection(data: dict) -> models.DatabaseConnection:
    """Serialize the given dictionary into a DatabaseConnection object."""

    database_connection = models.DatabaseConnection(
        user       = data.get('user') or None,
        host       = data.get('host') or None,
        database   = data.get('database') or None,
        password   = data.get('password') or None,
        name       = data.get('name') or None,
        created_on = data.get('created_on') or None,
    )

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


