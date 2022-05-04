from __future__ import annotations
from tables.domain import models
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
    except ValueError:
        pass

    return database_connection

