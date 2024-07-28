# Native imports
import logging


def init_logger():
    """
    Initialize logger for the CLI
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
