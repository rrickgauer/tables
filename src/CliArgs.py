
from __future__ import annotations
# from typing import List
import argparse


class CliArgs:

    def __init__(self):
        """Command line parser.
        """
        # setup the arg parser
        self.parser = argparse.ArgumentParser(description="View a MySQL Database Schema on the command line.")
        self.addArguments()
        self.args = self.parser.parse_args()

        self._tables = self.args.tables or list()
        self._save = self.args.save
        self._views = self.args.views
        self._deleteConfigFile = self.args.delete
        self._allTables = '*' in self.tables
        self._tableNames = len(self.tables) == 0
    

    def addArguments(self):
        self.parser.add_argument('-t', '--tables', nargs="+", help="List of tables to display, or * for all.")
        self.parser.add_argument('-s', '--save', action="store_true", help="Flag indicating to save the output to a text file.")
        self.parser.add_argument('-d', '--delete', action="store_true", help="Delete current database configuration file?")
        self.parser.add_argument('-v', '--views', action="store_false", help="Include views")

    @property
    def tables(self) -> list[str]:
        """List of tables to output.
        """
        return self._tables

    @property
    def save(self) -> bool:
        """Save the results to an output file?
        """
        return self._save
    
    @property
    def views(self) -> bool:
        """Include views in the output?
        """
        return self._views
    
    @property
    def deleteConfigFile(self) -> bool:
        """Delete the current configuration file?
        """
        return self._deleteConfigFile

    @property
    def allTables(self) -> bool:
        """Describe all tables?
        """
        return self._allTables

    @property
    def showTableNames(self) -> bool:
        """Only report a list of table names.
        """
        return self._tableNames

    
    def toDict(self) -> dict:
        """Returns the object as a dictionary

        Returns:
            dict: object as a dict
        """

        outDict = dict(tables=self.tables, save=self.save, allTables=self.allTables, showTableNames=self.showTableNames, deleteConfigFile=self.deleteConfigFile)
        return outDict