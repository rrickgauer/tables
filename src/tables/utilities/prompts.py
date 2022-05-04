from __future__ import annotations
from getpass import getpass
from tables.domain import models



def prompt_database_connection(conn: models.DatabaseConnection):
    """Prompt the user for any missing connection attributes."""

    if not conn.name:
        conn.name = input('Name: ')
    
    if not conn.host:
        conn.host = input('Host: ')

    if not conn.user:
        conn.user = input('User: ', )
    
    if not conn.database:
        conn.database = input('Database: ')

    if not conn.password:
        conn.password = getpass('Password: ')


def prompt_add_connection_replace_name(connection_name) -> bool:
    """Prompt the user for confirmation of replacing an existing connection name."""

    print(f'You already have a connection named "{connection_name}".')
    replace_response = input('Are you sure you want to replace it? (Y to continue): ')

    if replace_response.upper() != 'Y':
        print('Aborted!')
        return True
    
    return False