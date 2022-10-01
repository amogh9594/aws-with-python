import os
import boto3 
import zipfile
from zipfile import ZipFile
from subprocess import run

s_path = 'filename/'
bucket = 'bucketname'

run( 'curl --insecure -O -J enter_url',shell=True )

zp = zipfile.ZipFile("filename.zip")
size = sum([zinfo.file_size for zinfo in zp.filelist])
zip_kb = float(size) / 1000 

if zip_kb != 0:
    with ZipFile('filename.zip', 'r') as f:
        f.extractall()

    for i in os.listdir(r'filename'):
        isExist = os.path.exists(s_path)
        
        if isExist == True : 
            aws_filename = i
            print(i)

            f_path = s_path+aws_filename
            print(f_path)

            # Amazon AWS client
            s3 = boto3.client('s3', aws_access_key_id="xxxxxxxxxxxxxxxxxxxxx",aws_secret_access_key="xxxxxxxxxxxxxxxxxxxxxxxxx",region_name="xxxxxxxxxxxxx")
            s3.upload_file(f_path, bucket, aws_filename)   
            print("Uploading Successful")         
            os.remove(f_path)
        
        else :
            print("File Not Found") 
            
    os.remove("filename.zip")
    os.rmdir("filename")
    print("Delete Successful")

else:
    os.remove("filename.zip")
    print("File is Empty")
            
            
