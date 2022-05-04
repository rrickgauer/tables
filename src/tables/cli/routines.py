from __future__ import annotations
from .args import CliArgs
from tables.domain.models import DatabaseConnection, ViewCommandCliArgFlags
from tables.utilities import serializers

def get_database_connection(cli_args: CliArgs) -> DatabaseConnection:
    """Creat a new DatabaseConnection model with property values provided in the CLI args."""

    args_dict = cli_args.args.__dict__
    return serializers.to_database_connection(args_dict)


def get_view_command_cli_flags(cli_args: CliArgs) -> ViewCommandCliArgFlags:
    """Get the optional cli flag values for the view command."""
    
    args = cli_args.args.__dict__

    flags = ViewCommandCliArgFlags(
        all = args.get('all') or False,
        tables = args.get('tables') or False,
        views = args.get('views') or False,
    )

    return flags