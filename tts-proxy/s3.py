import boto3
from botocore.client import Config
from os import environ
import logging
from botocore.exceptions import ClientError,EndpointConnectionError
from io import BytesIO

logger = logging.getLogger("s3")

cloud_s3_client = boto3.client(
    "s3",
    endpoint_url=environ.get("CLOUD_S3_ENDPOINT"),
    aws_access_key_id=environ.get("CLOUD_S3_ACCESS_KEY"),
    aws_secret_access_key=environ.get("CLOUD_S3_SECRET_ACCESS_KEY"),
    region_name=environ.get("CLOUD_S3_REGION"),
)
logger.info("Cloud S3 storage init")

# Время жизни ссылки на файл
file_link_expiration = 9000
# Названия бакетов с файлами
cloud_bucket_name = environ.get("CLOUD_BUCKET_NAME")


def get_file_link(text_hash: str):
    try:
        response = cloud_s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": cloud_bucket_name, "Key": text_hash},
            ExpiresIn=file_link_expiration,
        )
    except ClientError as e:
        logger.error(e)
        return None
    return response

def is_file_exist(text_hash:str):
    try:
        cloud_s3_client.head_object(Bucket=cloud_bucket_name, Key=text_hash)
    except ClientError:
        return False
    return True

def get_cloud_file_link(text_hash: str):
    if is_file_exist(text_hash):
        return get_file_link(text_hash)
    else:
        return None

def upload_file(file,text_hash:str):
    fileobj = BytesIO(file)
    try:
        logger.info("Uploading file to cloud S3")
        cloud_s3_client.upload_fileobj(
            fileobj,
            cloud_bucket_name,
            text_hash
        )
        logger.info("Done")
    except Exception as e:
        print(e)
        logger.error(e)