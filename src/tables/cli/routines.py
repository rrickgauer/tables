from __future__ import annotations
from .args import CliArgs
from tables.domain.models import DatabaseConnection
from tables.utilities import serializers

def get_database_connection(cli_args: CliArgs) -> DatabaseConnection:
    """Creat a new DatabaseConnection model with property values provided in the CLI args."""

    args_dict = cli_args.args.__dict__
    return serializers.to_database_connection(args_dict)