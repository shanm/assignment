import os
import boto3

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket)

response = s3_client.list_objects_v2(Bucket='your-bucket-name')
objects = response.get('Contents', [])
for obj in objects:
    print(f"Object: {obj['Key']}, Size: {obj['Size']} bytes")
    
#Download a file from S3
file_name = 'test.jpg'
s3_client.download_file(Bucket='your-bucket-name', Key=file_name, Filename='downloaded_' + file_name)


# Versioning S3 files
s3_client.put_bucket_versioning(
    Bucket='your-bucket-name',
    VersioningConfiguration={
        'Status': 'Enabled'
    }
)

response = s3_client.list_object_versions(
    Bucket='your-bucket-name',
    Prefix='test.jpg'
    )

for version in response.get('Versions', []):
    print(f"Version ID: {version['VersionId']}, Is Latest: {version['IsLatest']}, Last Modified: {version['LastModified']}")
    
s3_client.download_file(
    Bucket='your-bucket-name',
    Key='test.jpg',
    Filename='downloaded_test.jpg',
    ExtraArgs={'VersionId': 'your_version_id'}  
) # Replace with the actual version ID you want to download


#Upload a file to S3
file_name = 'test.jpg'
s3_client.upload_file(Filename=file_name, Bucket='your-bucket-name', Key=file_name, ExtraArgs={'Metadata': {'custom-meta': 'value'}})  # Add custom metadata if needed

# Delete a file from S3
s3_client.delete_object(Bucket='your-bucket-name', Key='test.jpg')

# Empty a bucket (delete all objects) before deleting the bucket itself
bucket_name = 'your-bucket-name'
bucket = s3_resource.Bucket(bucket_name)
bucket.objects.all().delete()  # Delete all objects in the bucket
bucket.object_versions.all().delete()  # Delete all versions of objects in the bucket (if versioning is enabled)
s3_client.delete_bucket(Bucket=bucket_name)  # Delete the bucket itself
