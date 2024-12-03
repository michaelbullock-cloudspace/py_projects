import boto3

s3_resource = boto3.resource('s3')

bucket_name = 'mb-python-automation2'

# Create API CAll
s3_resource.create_bucket(Bucket=bucket_name)

print(f"{bucket_name} was created successfully!!!")