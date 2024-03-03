import logging
import os
from boto3 import client

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sqs = client("sqs")
SQS_QUEUE_URL = os.environ.get("SQS_QUEUE_URL")

def test_function():
    logger.info('Test function called')
    print("Test function called: Updated")
    sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody="hello world")


if __name__ == '__main__':
    test_function()
