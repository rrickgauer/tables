from __future__ import annotations
from tables.domain import models
from tables.domain import maps
from tables.persistence import data_access
from tables.utilities.serializers import to_database_connection
from tables.domain import constants


def get_connection(name) -> maps.DatabaseConnectionsMap | None:
    """Get the specified connection object from the storage file."""

    connections = get_connections_map()
    return connections.get(name) or None

def delete_connection(name):
    """Delete the specified connection from the storage file."""
    
    connections = get_connections_map()
    connections.pop(name)
    _save_connections_map(connections)


def does_connection_name_exist(name) -> bool:
    """Checks if the specified name already exists in the database connections file."""

    if name in _get_connections_names():
        return True
    else:
        return False


def get_connections_list() -> list[models.DatabaseConnection]:
    """Get a list of all the existing database connections."""

    return list(get_connections_map().values()) or []


def get_connections_map() -> maps.DatabaseConnectionsMap:
    """Get a map of all the existing database connections."""

    connections_map = {}
    for name, data_obj in data_access.read_database_connections().items():
        connections_map[name] = to_database_connection(data_obj)

    return connections_map


def add_new_connection(new_connection: models.DatabaseConnection):
    """Add the specified database connection to the storage file"""

    # get the existing map
    connections_map = get_connections_map()

    # add the new connection object to the collection
    connections_map[new_connection.name] = new_connection

    # save it to the file
    _save_connections_map(connections_map)

def _save_connections_map(connections: maps.DatabaseConnectionsMap):
    """Save the specified connections map to the json file."""

    output_file = constants.getAbs(constants.Files.CONNECTIONS)
    data_access.dump_json_to_file(connections, output_file)


def _get_connections_names() -> list[str]:
    """Get a list of all the connection names"""

    # get the existing map
    connections_map = get_connections_map()
    return list(connections_map.keys()) or []
