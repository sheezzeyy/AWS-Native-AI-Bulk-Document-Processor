import boto3
from botocore.exceptions import BotoCoreError, ClientError


REGION = "ap-south-1"
BUCKET_NAME = "aws-ai-bulk-docs-candidate-a"
TABLE_NAME = "documents"


def main():
    s3 = boto3.client("s3", region_name=REGION)
    dynamodb = boto3.client("dynamodb", region_name=REGION)

    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
        print(f"SUCCESS: S3 bucket '{BUCKET_NAME}' is accessible.")
    except (BotoCoreError, ClientError) as error:
        print(f"FAILURE: Could not access S3 bucket '{BUCKET_NAME}': {error}")

    try:
        dynamodb.describe_table(TableName=TABLE_NAME)
        print(f"SUCCESS: DynamoDB table '{TABLE_NAME}' is accessible.")
    except (BotoCoreError, ClientError) as error:
        print(f"FAILURE: Could not access DynamoDB table '{TABLE_NAME}': {error}")


if __name__ == "__main__":
    main()
