import boto3

# Use Amazon S3
client = boto3.client('s3')
response = client.delete_bucket(
    Bucket='berkanovic-boto3-bucket',
)

print(response)
