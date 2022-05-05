"""
************************************************************************************

Command line arguments parser.

The new cli design has 4 commands:
    - list: prints out all the stored connections
    - add: create/save a new connection
    - view: view a saved connection
    - delete: delete a saved connection

Each command has its own seperate set of flags/arguments.

***************************************************************************************
"""

from __future__ import annotations
import argparse
from tables.domain.enums import CliCommands
from .choices import VIEW_COLUMN_CHOICES_ALL

class CliArgs:

    def __init__(self):
        """Constructor"""

        self._parser = argparse.ArgumentParser(description="Display your mysql database table schemas")
        self.args = None
        self._subparser = None

    def parse(self):
        """Parse the command line arguments"""

        self._add_arguments()
        self.args = self._parser.parse_args()

    def _add_arguments(self):
        """Add all the arguments to the parser"""

        # create a command subparser
        self._subparser = self._parser.add_subparsers(dest='command')

        # add each of the command flag arguments
        self._add_subparser_list()
        self._add_subparser_add()
        self._add_subparser_delete()
        self._add_subparser_view()
        

    def _add_subparser_list(self):
        """Add the cli flag arguments for the list command."""

        sub_parser = self._subparser.add_parser(CliCommands.LIST.value)


    def _add_subparser_add(self):
        """Add the cli flag arguments for the add command."""

        sub_parser = self._subparser.add_parser(CliCommands.ADD.value)
        sub_parser.add_argument('--name', type=str, required=False)
        sub_parser.add_argument('--user', type=str, required=False)
        sub_parser.add_argument('--host', type=str, required=False)
        sub_parser.add_argument('--database', type=str, required=False)
        sub_parser.add_argument('--password', type=str, required=False)


    def _add_subparser_delete(self):
        """Add the cli flag arguments for the delete command."""

        sub_parser = self._subparser.add_parser(CliCommands.DELETE.value)
        sub_parser.add_argument('--name', type=str, required=False)


    def _add_subparser_view(self):
        """Add the cli flag arguments for the view command."""

        sub_parser = self._subparser.add_parser(CliCommands.VIEW.value)
        sub_parser.add_argument('-n', '--name', type=str, required=False, help="Database connection name.")

        sub_parser.add_argument('-a', '--all', action="store_true", help="Dump table and view schemas.")
        sub_parser.add_argument('-t', '--tables', action="store_true", help="Dump table schemas.")
        sub_parser.add_argument('-v', '--views', action="store_true", help="Dump view schemas.")

        sub_parser.add_argument('-c', '--columns', choices=VIEW_COLUMN_CHOICES_ALL, nargs="+", type=str, action="extend", metavar='')

    @property
    def command(self) -> CliCommands:
        """Get the command."""

        try:
            command = CliCommands(self.args.command)
        except ValueError:
            command = CliCommands.LIST

        return command

        