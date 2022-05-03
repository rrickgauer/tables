"""
********************************************************************************************

This is the main entry point for the entire application.

********************************************************************************************
"""

from tables.cli import CliArgs
from tables.data_access import read_database_connections

def run():
    """Main entry point"""

    cli_args = CliArgs()
    cli_args.parse()
    print(cli_args.command)


    existing_connections = read_database_connections()

    for connection in existing_connections:
        print("\n\n")
        for key, value in connection.items():
            print(f'{key}: {value}')
    