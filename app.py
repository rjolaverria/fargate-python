import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_function():
    logger.info('Test function called')
    print("Test function called: Updated")


if __name__ == '__main__':
    test_function()
