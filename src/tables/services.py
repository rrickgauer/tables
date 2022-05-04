from __future__ import annotations
from tables.domain import models
from tables.domain import maps
from tables.data_access import read_database_connections
from tables.serializers import to_database_connection

def get_existing_connections_map() -> maps.DatabaseConnectionsMap:
    """Get a map of all the existing database connections."""

    connections = {conn.name: conn for conn in get_existing_connections_list()}
    return connections

def get_existing_connections_list() -> list[models.DatabaseConnection]:
    """Get a list of all the existing database connections."""

    existing_connections = [to_database_connection(d) for d in read_database_connections()]
    return existing_connections