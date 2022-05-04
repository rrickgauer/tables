from __future__ import annotations
from getpass import getpass
from tables.domain import models



def prompt_database_connection(conn: models.DatabaseConnection):
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