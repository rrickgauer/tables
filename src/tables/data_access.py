from __future__ import annotations
import json
from json import JSONDecodeError
from opcode import opname
from tables.constants import getAbs, Files



def read_database_connections() -> list[dict]:
    """Retrieve the data from the connections json file."""

    data_file_path = getAbs(Files.CONNECTIONS)
    json_data = _read_json_file(data_file_path) or []
    return json_data


def _read_json_file(file_name) -> dict | list | None:
    """Read in the specified file as a json object"""

    try:
        json_file = open(file_name, 'r')
    except FileNotFoundError:
        json_file.close()
        _create_empty_file(file_name, '[]')
        return None

    try:
        data = json.loads(json_file.read())
    except JSONDecodeError as ex:
        print(f'Error reading the file: {file_name}')
        data = None
    finally:
        json_file.close()

    return data


def _create_empty_file(file_name, output):
    with open(file_name, 'w') as new_file:
        new_file.write(output)
    

    
