import logging
import inspect
import os


def get_logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    if not logger.handlers:
        if not os.path.exists("logs"):
            os.makedirs("logs")

        fileHandler = logging.FileHandler('logs/automation.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)

    return logger