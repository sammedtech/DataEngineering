import json
import sys
import boto3

from utils.validation_functions import get_header_count
# from utils.database import get_redshift_header_count

########################################################################################
# following part of code should be created in different validation_functions.py file
import csv
import boto3

def get_header_count(bucket_name, file_name) :
    # Open and read the CSV file using csv.reader
    s3 = boto3.client('s3')
    
    # Download the CSV file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    csv_data = response['Body'].read().decode('utf-8')
    
    # Create a CSV reader with the semicolon separator
    csv_reader = csv.reader(csv_data.splitlines(), delimiter=';')
    
    # Read the header row and count the number of columns
    header = next(csv_reader)
    input_file_header_count = len(header)
    return input_file_header_count
##########################################################################################

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    file_type = file_name.split("/")[2].split("_")[2].lower()
    erp_system = file_name.split("/")[1].lower()
    file_key = file_name.split("/")[2]
    release_timestamp = event['Records'][0]['eventTime']

    destination_bucket = "sammedtech-working-zone"
    output_path = f"s3://{destination_bucket}/raw/{erp_system}/{release_timestamp}/{file_type}/"
    
    print("file name : ", file_name)
    print("file type : ", file_type)
    
    source_file_path = f"s3://{bucket_name}/{file_name}"
    print("source_file_path : ", source_file_path)
    
    input_file_header_count = get_header_count(bucket_name, file_name)
    print("header_count : ", input_file_header_count)
    
    redshift_header_count = {'ap' : 28, 'suppliermaster' : 11, 'companymaster' : 10, 'paymenttermmaster' : 33, 'customermaster' : 9, 'ar' : 22}
    
    if input_file_header_count == redshift_header_count[file_type] :
        print("Column count Succeeded..")
        s3_client = boto3.client('s3')
        
        copy_source = {'Bucket':bucket_name, 'Key':file_name}
        
        response = s3_client.list_objects_v2(Bucket=destination_bucket,Prefix=f"raw/{erp_system}{file_type}/")
        if 'Contents' in response:
            objects = [{'Key':obj['Key']} for obj in response['Contents']]
            s3_client.delete_objects(Bucket=destination_bucket,Delete={'Objects':objects})
                    
        s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=f"raw/{erp_system}/{file_type}/{file_key}")
    else : 
        print("Failed. Header count not matched.")
    
    
    