"""
********************************************************************************************

This is the main entry point for the entire application.

********************************************************************************************
"""

from tables.cli import CliArgs

def run():
    """Main entry point"""

    cli_args = CliArgs()
    cli_args.parse()
    print(cli_args.command)