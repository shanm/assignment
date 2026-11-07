import boto3

#Initialize a session using Amazon S3
s3 = boto3.client('s3')

bucket_name = 'your-bucket-name'

# Create a new bucket
#s3.create_bucket(Bucket=bucket_name, create_bucket_configuration={'LocationConstraint': 'us-west-2'})
#print(f"Bucket '{bucket_name}' created successfully.")

file_name = 'test.jpg'
#s3.upload_file(file_name, bucket_name, file_name)
#print(f"File '{file_name}' uploaded to bucket '{bucket_name}' successfully.")

#s3.download_file(bucket_name, file_name, 'downloaded_' + file_name)
#print(f"File '{file_name}' downloaded from bucket '{bucket_name}' successfully.")

response = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(f"Object: {obj['Key']}, Size: {obj['Size']} bytes")

# Print the list of existing buckets
for bucket in s3.buckets.all():
    print(bucket['Name'])