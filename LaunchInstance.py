def main():
    import boto3

    REGION = 'ap-south-1'        # region to launch instance.
    AMI = 'ami-074dc0a6f6c764218'        # AMI of the Virtual Machine
    INSTANCE_TYPE = 't2.micro'  # instance type to launch.
    EC2 = boto3.resource('ec2', region_name=REGION)

    instance = EC2.create_instances(        # Creating Instance
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        MinCount=1,                         
        MaxCount=1,
        InstanceInitiatedShutdownBehavior='stop', # shutdown behaviour of the EC2 instance
    )

    print ("New Instance Created With ID:",instance[0].instance_id)
    
    EC2.create_tags(Resources=[instance[0].instance_id], Tags=[{'Key':'Name', 'Value':'lambda ec2'}])       #Tag A Name To New Instance
    
    return instance[0].instance_id

def lambda_handler(event, context):
    print("New Instance ID: {}".format(main()))
    return None
