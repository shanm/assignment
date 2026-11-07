import json
import boto3

client = boto3.client('lambda')

response = client.invoke(
    FunctionName='your_lambda_function_name',
    payload=json.dumps({"key": "value"}).encode('utf-8')
)

print(response['Payload'].read().decode('utf-8'))