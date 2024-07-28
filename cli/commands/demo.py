# Native imports
import logging

# 3rd party imports
import click

logger = logging.getLogger()


@click.command("sum")
@click.option("--num1", type=int, required=True)
@click.option("--num2", type=int, required=True)
def cmd_sum(num1: int, num2: int):
    """
    Sum two numbers.
    """
    logger.info("Sum of %s and %s is %s", num1, num2, num1 + num2)
