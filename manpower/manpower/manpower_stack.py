from aws_cdk import (
    aws_s3 as s3,
    core as core
)


class ManpowerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self,
            "MyFirstBucket",
            versioned=True,
            public_read_access=True,
            removal_policy=core.RemovalPolicy.DESTROY
        );