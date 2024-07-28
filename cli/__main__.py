# 3rd party imports
import click

# Project imports
from cli import __version__
from cli.common.logger import init_logger
from cli.commands import *  # pylint: disable=W0401

init_logger()


@click.group()
@click.version_option(__version__.version)
def cli():
    """
    CLI template for Python projects.
    """


# Add commands to the CLI
cli.add_command(cmd_sum)

if __name__ == "__main__":
    cli()
