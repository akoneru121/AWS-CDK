from aws_cdk import aws_ec2 as ec2
from constructs import Construct

def create_ec2(scope: Construct, vpc: ec2.Vpc) -> ec2.Instance:
    instance = ec2.Instance(
        scope, "WebAppInstance",
        instance_type=ec2.InstanceType("t2.micro"),
        machine_image=ec2.MachineImage.latest_amazon_linux2(),
        vpc=vpc,
        vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
    )
    
    # Add security group allowing HTTP and SSH access
    instance.connections.allow_from_any_ipv4(ec2.Port.tcp(22), "SSH access")
    instance.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "HTTP access")
    
    instance.node.default_child.tags.set_tag("Name", "WebAppInstance")
    return instance
