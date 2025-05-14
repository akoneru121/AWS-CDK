from aws_cdk import Stack
from constructs import Construct
from .vpc import create_vpc
from .ec2_instance import create_ec2
from .rds import create_rds
from .s3_bucket import create_s3_bucket
#from .route53 import create_route53

class MyWebAppStack(Stack):
    
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # Create VPC
        vpc = create_vpc(self)

        # EC2 instance
        ec2_instance = create_ec2(self, vpc)
        
        # RDS instance
        create_rds(self, vpc)

        # S3 bucket
        create_s3_bucket(self)

        # Route 53 setup
        #create_route53(self, vpc, ec2_instance)
