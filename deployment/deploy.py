import boto3
import sys

boto3.client("lambda").invoke(
    FunctionName="ecs-deploy",
    InvocationType="Event",
    Payload=open(f"deployment/{sys.argv[1]}.json").read(),
)
