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

class CliArgs:

    def __init__(self):
        """Constructor"""

        self._parser = argparse.ArgumentParser(description="Display your mysql database table schemas")
        self._args = None
        self._subparser = None

    def parse(self):
        """Parse the command line arguments"""

        self._add_arguments()
        self._args = self._parser.parse_args()

    def _add_arguments(self):
        """Add all the arguments to the parser"""

        # create a command subparser
        self._subparser = self._parser.add_subparsers(dest='command')

        # add each of the command flag arguments
        self._add_subparser_list()
        self._add_subparser_add()
        

    def _add_subparser_list(self):
        """Add the cli flag arguments for the list command."""

        sub_parser = self._subparser.add_parser(CliCommands.LIST.value)
        sub_parser.add_argument('--username', type=str)

    def _add_subparser_add(self):
        """Add the cli flag arguments for the add command."""

        sub_parser = self._subparser.add_parser(CliCommands.ADD.value)
        # sub_parser.add_argument('--username', type=str)


    @property
    def command(self) -> CliCommands:
        """Get the command."""

        try:
            command = CliCommands(self._args.command)
        except ValueError:
            command = CliCommands.LIST

        return command

        

    
    

        