"""
************************************************************************************

This is class for the command line argument parser.

***************************************************************************************
"""

from __future__ import annotations
import argparse

class CliArgs:

    def __init__(self):
        """Constructor"""

        self._parser = argparse.ArgumentParser(description="Display your mysql database table schemas")
        self._args = None

    def parse(self):
        """Parse the command line arguments"""

        self._add_arguments()
        self._args = self._parser.parse_args()

    def _add_arguments(self):
        """Add all the arguments to the parser"""
        
        # self._parser.add_argument('-d', '--development', action="store_false", help=ArgumentDescriptions.DEVELOPMENT_FLAG)
        pass

    
    

        