import boto3
import logging





def create_ec2_instance():
    """
    This program uses a Python function and boto3 to create an EC2 instance with the name ec2-created-by-python.
    - Provide an on Linux 2 AMI
    - Use t3.micro instance type
    - Use best practices, logging handle exception, us variables, use main, doc strings etc. 

    """

    # Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
AMI_ID = 'ami-0166fe664262f664c'  # Amazon Linux 2 AMI ID for your N. Virginia region
INSTANCE_TYPE = 't3.micro'
INSTANCE_NAME = 'ec2-created-by-python'



def create_ec2_instance():
    """
    Creates an EC2 instance using the specified parameters.
    """
    ec2_client = boto3.client('ec2')
    try:
        logging.info("Creating EC2 instance...")
        response = ec2_client.run_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': INSTANCE_NAME}
                    ]
                }
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        logging.info(f"EC2 instance created successfully with Instance ID: {instance_id}")
        return instance_id
    except Exception as e:
        logging.error(f"An error occurred while creating the EC2 instance: {e}")
        return None

def main():
    """
    Main function to create an EC2 instance.
    """
    instance_id = create_ec2_instance()
    if instance_id:
        logging.info(f"Instance {instance_id} is up and running!")

if __name__ == "__main__":
    main()
