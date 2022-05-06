
from __future__ import annotations
from .args import CliArgs
from tables.domain.models import DatabaseConnection
from tables.domain.models import ViewCommandCliArgFlags
from tables.utilities import serializers

def get_database_connection(cli_args: CliArgs) -> DatabaseConnection:
    """Creat a new DatabaseConnection model with property values provided in the CLI args."""

    args_dict = cli_args.args.__dict__
    return serializers.to_database_connection(args_dict)


def get_view_command_cli_flags(cli_args: CliArgs) -> ViewCommandCliArgFlags:
    """Get the optional cli flag values for the view command."""
    
    args = cli_args.args.__dict__
    return serializers.serialize_view_command_cli_arg_flags(args)
