from aws_cdk import aws_ec2 as ec2
from constructs import Construct

def create_vpc(scope: Construct) -> ec2.Vpc:
    return ec2.Vpc(
        scope, "MyVPC",
        max_azs=2,
        subnet_configuration=[
            ec2.SubnetConfiguration(
                name="PublicSubnet",
                subnet_type=ec2.SubnetType.PUBLIC,
                cidr_mask=24
            ),
            ec2.SubnetConfiguration(
                name="PrivateSubnet",
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                cidr_mask=24
            ),
        ],
        nat_gateways=1
    )
