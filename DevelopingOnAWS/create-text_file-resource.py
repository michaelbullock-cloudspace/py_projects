# Write a function to create a text file called python-on-aws.txt, write on the file the text below: 
# "programming is fun, but you got to practice". 
# Write another the function to upload the file created previously to any existing S3 bucket on AWS.

import boto3
import logging

# setup logger
# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(filename='myapp.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

def create_file():
    """
    Creates a file and writes the text "programming is fun you got to practice" into it.
    
    Returns:
    - str: The name of the created file.
    """
    filename = 'my_file.txt'
    text = "programming is fun you got to practice"
    
    try:
        with open(filename, 'w') as file:
            file.write(text)
        # print(f"File '{filename}' created with the text: {text}")
        logger.info(f"File '{filename}' created with the text: {text}")
    except Exception as e:
        # print(f"An error occurred while creating or writing to the file '{filename}': {e}")
        logger.error(f"An error occurred while creating or writing to the file '{filename}': {e}")
    
    return filename

def upload_file_to_s3(filename, bucket_name):
    """
    Uploads the specified file to an existing S3 bucket on AWS.
    
    Parameters:
    - filename: str, the name of the file to upload
    - bucket_name: str, the name of the S3 bucket to upload to
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    try:
        # Upload the file to the specified S3 bucket
        s3_client.upload_file(filename, bucket_name, filename)
        # print(f"File '{filename}' successfully uploaded to bucket '{bucket_name}'.")
        logger.info(f"File '{filename}' successfully uploaded to bucket '{bucket_name}'.")
    except Exception as e:
        # print(f"Failed to upload '{filename}' to bucket '{bucket_name}': {e}")
        logger.error(f"Failed to upload '{filename}' to bucket '{bucket_name}': {e}")

# main
if __name__ == "__main__":

    # 1. Create the file with the specific text
    filename = create_file()

    # 2. Upload the file to an existing S3 bucket
    upload_file_to_s3(filename, 'complex-or-challenging-bucket-01')

    logger.info(f"this is the end!!!")