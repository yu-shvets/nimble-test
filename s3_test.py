import boto3
from aws_credentials import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import requests
from botocore.exceptions import ClientError

BUCKET_NAME = 'nimble-test'
FILE_NAME = 'test.jpg'


# A function to create S3 client
def get_s3_client():
    return boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


# A function to put a binary file to existing S3 bucket
def put_file(bucket_name, file_name):
    s3_client = get_s3_client()
    url = s3_client.generate_presigned_url('put_object', Params={'Bucket': bucket_name, 'Key': file_name})
    requests.put(url, data=open(file_name, 'rb'))


# A function to download file from existing S3 bucket
def get_file(bucket_name, file_name):
    s3_client = get_s3_client()
    try:
        s3_client.download_file(bucket_name, file_name, 'downloads/{}'.format(file_name))
    except ClientError:
        print('File not found')
