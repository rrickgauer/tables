

from tables import constants
from tables.cli import CliArgs


# main entry point
def run():
    connections = constants.getAbs(constants.Files.CONNECTIONS)
    print(connections)

    cli_args = CliArgs()
    cli_args.parse()