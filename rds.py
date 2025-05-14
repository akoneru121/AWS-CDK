from aws_cdk import aws_rds as rds
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

def create_rds(scope: Construct, vpc: ec2.Vpc) -> rds.DatabaseInstance:
    db_instance = rds.DatabaseInstance(
        scope, "MyDBInstance",
        engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0_23),
        instance_type=ec2.InstanceType("t2.micro"),
        vpc=vpc,
        vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
        multi_az=False,
        allocated_storage=20,
        max_allocated_storage=100,
        storage_encrypted=True,
        publicly_accessible=False,
    )

    db_instance.node.default_child.tags.set_tag("Name", "MyDBInstance")
    return db_instance
