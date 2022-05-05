"""
********************************************************************************************

This is the main entry point for the entire application.

********************************************************************************************
"""
from __future__ import annotations
from datetime import datetime
from tables import cli
from tables.domain.enums import CliCommands
from tables.persistence import services
from tables.utilities import printers
from tables.utilities import prompts
from tables.utilities.routines import set_pymysql_credentials
from tables.commands import ViewCommand

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
    output = printers.print_dataclasses(connections)
    print(f'\n{output}')


def _run_command_view(cli_args: cli.CliArgs):
    """Run the list command
    
    You can either output:
        - the list of tables/views
        - dump all the tables and views schemas
        - dump the table schemas
        - dump the view schemas
    """

    # prompt user for connection name if it was not provided in the cli args
    connection_name = cli_args.args.name or input('Name: ')

    # check if the connection name exists
    if not services.does_connection_name_exist(connection_name):
        print(f'You do not have a connection named "{connection_name}".')
        return
    
    # setup the database credentials so we can fetch the table schemas
    database_connection = services.get_connection(connection_name)
    set_pymysql_credentials(database_connection)
    view_command = ViewCommand(database_connection.database)
    view_command.load_tables()

    # determine which dump we should do
    command_args = cli.get_view_command_cli_flags(cli_args)

    # print list of tables/view
    if True not in [command_args.all, command_args.tables, command_args.views]:
        print(printers.print_dataclasses(view_command.dump_tables_list()))
        return 

    # dump all
    if command_args.all:
        command_args.tables = False
        command_args.views  = False

    # both -v and -t flags were set, so just pretend like its a dump all
    elif False not in [command_args.tables, command_args.views]:
        command_args.all    = True
        command_args.tables = False
        command_args.views  = False

    if command_args.views:
        dump = view_command.dump_views()
    elif command_args.tables:
        dump = view_command.dump_tables()
    else:
        dump = view_command.dump_all()


    table_columns = cli.get_view_command_columns(cli_args)

    print(printers.dump_json(dump))
        

    
    

    
        
    


    