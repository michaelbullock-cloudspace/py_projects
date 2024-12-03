import boto3
import botocore
import csv
import logging

# Setup loggers
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Global variable
REPORT_NAME = 'ec2_report.csv'

def list_all_ec2_instances():
    """
    Gather all EC2 instances and return a list of dictionaries.
    :return: List of dictionaries containing instance details.
    """
    # Initialize client
    ec2_client = boto3.client('ec2')

    # Response
    response = ec2_client.describe_instances()

    # Retrieve the list of instances
    reservations = response['Reservations']  # List with dictionaries

    # List to hold instance details
    list_ec2_instances = []

    # Looping through the reservations
    for reservation in reservations:
        # Loop through the instances in each reservation
        for instance in reservation["Instances"]:
            instance_data = {
                'instance_name': instance["Tags"][0]['Value'] if 'Tags' in instance else "No Name",
                'instance_type': instance["InstanceType"],
                'image_id': instance["ImageId"],
                'state': instance["State"]["Name"]
            }
            # Add the dictionary to the list
            list_ec2_instances.append(instance_data)

    return list_ec2_instances

def generate_csv_report(instances):
    """
    Generate a CSV report using DictWriter.
    :param instances: List of dictionaries with instance details.
    :return: True if the report is successfully generated, else False.
    """
    try:
        with open(REPORT_NAME, 'w', newline='') as csvfile:
            fieldnames = ['instance_name', 'instance_type', 'image_id', 'state']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header
            csvwriter.writeheader()

            # Write the data
            csvwriter.writerows(instances)
    except OSError as error:
        logger.error(f"File creation failed: {error}")
        return False
    return True

def upload_report_to_s3():
    """
    Upload the CSV report to an S3 bucket.
    """
    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(REPORT_NAME, 'i-love-eating-fufu-with-spicy-goat-meat', REPORT_NAME)
    except botocore.exceptions.ClientError as error:
        logger.error(f"Failed to upload the file: {error}")

# Main
if __name__ == '__main__':
    # Retrieve EC2 instances
    instances = list_all_ec2_instances()

    logger.info(f'Generating CSV report: {REPORT_NAME}')
    # Generate report
    if generate_csv_report(instances):
        logger.info(f'Uploading report to S3')
        # Upload report
        upload_report_to_s3()

    logger.info('Good night folks!!!')
