import logging
import sys


def setup_logger(name=__name__):
    # create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler("data/logging.log")
    
    # Add formatters
    c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Test")
