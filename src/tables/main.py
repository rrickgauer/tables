"""
********************************************************************************************

This is the main entry point for the entire application.

********************************************************************************************
"""
from __future__ import annotations
from datetime import datetime
from tables import cli
from tables.domain.enums import CliCommands
from tables import services
from tables import printers
from tables import prompts

def run():
    """Main entry point"""

    cli_args = cli.CliArgs()
    cli_args.parse()

    if cli_args.command == CliCommands.ADD:
        _run_command_add(cli_args)
    elif cli_args.command == CliCommands.DELETE:
        _run_command_delete(cli_args)
    elif cli_args.command == CliCommands.VIEW:
        _run_command_view(cli_args)
    else:
        _run_command_list()
    

def _run_command_add(cli_args: cli.CliArgs):
    """Run the add command"""

    # get any cli args for the new connection that were provided in the cli
    new_connection = cli.get_database_connection(cli_args)
    new_connection.created_on = datetime.now()

    # fill in any missing required attributes by prompting the user for input
    prompts.prompt_database_connection(new_connection)

    # validate
    if services.does_connection_name_exist(new_connection.name):
        if prompts.prompt_add_connection_replace_name(new_connection.name):
            return

    # save the new connection to the file
    services.add_new_connection(new_connection)

    print('Added successfully!')


def _run_command_delete(cli_args: cli.CliArgs):
    """Run the delete command."""
    
    # prompt user for connection name if it was not provided in the cli args
    connection_name = cli_args.args.name or input('Name: ')

    # check if the connection name exists
    if not services.does_connection_name_exist(connection_name):
        print(f'You do not have a connection named "{connection_name}".')
        return
    
    # delete it from the storage file
    services.delete_connection(connection_name)
    print('Removed!')
    

def _run_command_list():
    """Run the list command"""

    connections = services.get_connections_list()
    output = printers.get_database_connections(connections)
    print(f'\n{output}')


def _run_command_view(cli_args: cli.CliArgs):
    # prompt user for connection name if it was not provided in the cli args
    connection_name = cli_args.args.name or input('Name: ')

    # check if the connection name exists
    if not services.does_connection_name_exist(connection_name):
        print(f'You do not have a connection named "{connection_name}".')
        return

    database_connection = services.get_connection(connection_name)

    print(database_connection)

    