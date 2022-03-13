import os
import boto3
#import botocore


#initiate s3 resource
#s3 = boto3.resource('s3')
s3 = boto3.resource('s3', aws_access_key_id='aws_access_key_id',aws_secret_access_key='aws_secret_access_key')
# select bucket
my_bucket = s3.Bucket('my_bucket')

# download file into current directory
items=[]
for s3_object in my_bucket.objects.all():
    print("Download files list from s3 bucket... ")
    print(s3_object.key)
    str = s3_object.key

    # Need to split s3_object.key into path and file name, else it will give error file not found.
    path, filename = os.path.split(s3_object.key)
    my_bucket.download_file(s3_object.key, str)

    

       


