from aws_cdk import aws_s3 as s3
from constructs import Construct

def create_s3_bucket(scope: Construct) -> s3.Bucket:
    bucket = s3.Bucket(
        scope, "MyWebAppBucket",
        versioned=True,
        removal_policy=s3.RemovalPolicy.DESTROY  # Don't forget to destroy on CDK destroy
    )
    return bucket
