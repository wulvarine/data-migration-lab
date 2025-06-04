import boto3
import pandas as pd
def upload_file_to_s3(local_file_path, bucket_name, s3_key=None):
    """Upload a file to an S3 bucket"""
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(local_file_path, bucket_name, s3_key)
    except Exception as e:
        print(f"Error uploading file: {e}")
    else:
        print(f"File {local_file_path} uploaded to {bucket_name} with key {s3_key}")
def download_file_from_s3(bucket_name, s3_key, local_file_path):
    """Download a file from an S3 bucket"""
    s3_client = boto3.client('s3')
    try:
        response = s3_client.download_file(bucket_name, s3_key, local_file_path)
    except Exception as e:
        print(f"Error downloading file: {e}")
    else:
        print(f"File {s3_key} downloaded from {bucket_name} to {local_file_path}")
if __name__ == "__main__":
    # Upload a file
    local_file_path = r"C:\aws_study_materials\data_folder\testdata.csv"  # <-- Note the raw string (r"")
    bucket_name = "dtinput"
    s3_key = "testdata.csv"
    upload_file_to_s3(local_file_path, bucket_name, s3_key)
    # Upload a file
    local_file_path = r"C:\aws_study_materials\data_folder\downloaded_testdata.csv"  # <-- Note the raw string (r"")
    bucket_name = "dtinput"
    s3_key = "testdata.csv"
    download_file_from_s3(bucket_name, s3_key, local_file_path)
    # Read the downloaded file into a DataFrame                                 
    df = pd.read_csv(local_file_path)
    print(df.head())  # Display the first few rows of the DataFrame