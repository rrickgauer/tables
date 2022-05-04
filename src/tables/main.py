"""
********************************************************************************************

This is the main entry point for the entire application.

********************************************************************************************
"""
from __future__ import annotations
from tables.cli import CliArgs
from tables.domain.enums import CliCommands
from tables import services
from tables import printers

def run():
    """Main entry point"""

    cli_args = CliArgs()
    cli_args.parse()

    if cli_args.command == CliCommands.LIST:
        _run_command_list()

def _run_command_list():
    """Run the list command"""

    connections = services.get_existing_connections_list()
    print("\n")
    print(printers.get_database_connections(connections))

    