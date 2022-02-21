import boto3

def iamaction():
    iam = boto3.resource('iam')
    groups = iam.Group('admins').users.all()
    names = [i.name for i in groups]
    return names

def lambda_handler(event, context):
    return iamaction()