import boto3
import botocore
from trp import Document
from textractcaller import call_textract_analyzeid

# S3 Bucket Data
s3BucketName = "aws-textract-invoice"
PlaindocumentName = "invoice-1.jpg"
#FormdocumentName = "Test3.JPG"
#TabledocumentName = "Test4.JPG"

# Amazon Textract client
#textractmodule = boto3.client('textract')
textractmodule = boto3.client("textract", aws_access_key_id=" ",
                              aws_secret_access_key=" ", region_name="us-east-1")

#1. PLAINTEXT detection from documents:
response = textractmodule.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': PlaindocumentName
        }
    })
print ('------------- Print Plaintext detected text ------------------------------')
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print ('\033[92m'+item["Text"]+'\033[92m')


#2. FORM detection from documents:
response = textractmodule.analyze_document(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': PlaindocumentName
        }
    },
    FeatureTypes=["FORMS"])
doc = Document(response)
print ('------------- Print Form detected text ------------------------------')
for page in doc.pages:
    for field in page.form.fields:
        print("Key: {}, Value: {}".format(field.key, field.value))



#2. TABLE data detection from documents:
response = textractmodule.analyze_document(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': PlaindocumentName
        }
    },
    FeatureTypes=["TABLES"])
doc = Document(response)
print ('------------- Print Table detected text ------------------------------')
for page in doc.pages:
    for table in page.tables:
        for r, row in enumerate(table.rows):
            itemName  = ""
            for c, cell in enumerate(row.cells):
                print("Table[{}][{}] = {}".format(r, c, cell.text))
