from __future__ import annotations
import json
from json import JSONDecodeError
from tables.domain.constants import getAbs, Files
from .json_encoder import CustomJSONEncoder
import os

def read_database_connections() -> dict:
    """Retrieve the data from the connections json file."""

    data_file_path = getAbs(Files.CONNECTIONS)
    json_data = _read_json_file(data_file_path) or {}
    return json_data


def _read_json_file(file_name) -> dict | list | None:
    """Read in the specified file as a json object"""

    try:
        json_file = open(file_name, 'r')
    except FileNotFoundError:
        # json_file.close()
        write_to_file(file_name, '{}')
        return None

    try:
        data = json.loads(json_file.read())
    except JSONDecodeError as ex:
        print(f'Error reading the file: {file_name}')
        data = None
    finally:
        json_file.close()

    return data


def dump_json_to_file(output, file_name):
    """Encode the given output to json and save it to a file."""

    json_string = json.dumps(output, indent=4, cls=CustomJSONEncoder)
    write_to_file(file_name, json_string)


def write_to_file(file_name, output):
    """Create a new file with the specified output"""

    _ensure_file_directory(file_name)

    with open(file_name, 'w') as new_file:
        new_file.write(output)

    

def _ensure_file_directory(file_name):
    """Make sure the directory exists for the specified file."""

    directory = os.path.dirname(file_name)
    
    if not os.path.exists(directory):
        os.mkdir(directory)

