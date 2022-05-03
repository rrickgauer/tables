from __future__ import annotations
import json
from tables.constants import getAbs, Files



def read_database_connections() -> list[dict]:
    data_file = getAbs(Files.CONNECTIONS)
    return read_json_file(data_file)

def read_json_file(file_name):
    json_file = open(file_name, 'r')

    try:
        data = json.loads(json_file.read())
    except:
        data = None
    finally:
        json_file.close()

    return data

    
