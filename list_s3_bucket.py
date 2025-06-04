import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket["Name"])
s3.upload_file('blank.txt', 'vindatabucket', r'"C:\AWS study materials\Data folder\blank.txt"')