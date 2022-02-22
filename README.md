# AWS With Python
The AWS SDK for Python (Boto3) enables you to use Python code to interact with AWS services like Amazon S3. For example, you can use the SDK to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created.

## AWS SDK for Python (Boto3)
Get started quickly using AWS with boto3, the AWS SDK for Python. Boto3 makes it easy to integrate your Python application, library, or script with AWS services including Amazon S3, Amazon EC2, Amazon DynamoDB, and more.

Install Package 
```
pip install boto3
```

## Program Files 
1. [AWS S3 Bucket Connection](https://github.com/amogh9594/aws-with-python/blob/main/aws_textract_invoice_ocr/api.py)
   * Set up credentials to connect Python to S3.
   * Authenticate with boto3.
   * Read and write data from/to S3.
 
2. [Analyzing Invoice Data Using Textract](https://github.com/amogh9594/aws-with-python/blob/main/aws_textract_invoice_ocr/api.py)
   * PLAINTEXT detection from documents.
   * FORM detection from documents.
   * TABLE data detection from documents.

3. [Lambda iam user call for AWS interaction](https://github.com/amogh9594/aws-with-python/blob/main/aws_lambda/lambda_iam_user_call.py)
   * AWS Identity and Access Management (IAM) user is an entity that you create in AWS to represent the person or application that uses it to interact with AWS.
   * The examples listed on this page are code samples written in Python that demonstrate how to interact with AWS Identity and Access Management (IAM).
   
4. [Using lambda read file from s3 using lambda trigger](https://github.com/amogh9594/aws-with-python/blob/main/aws_lambda/lambda_read_file_s3_trigger.py)
   * S3 Object Lambda gives you the flexibility to invoke Lambda functions directly from S3 GET requests to process data to meet the specific requirements of your   
     applications. 
   * S3 Object Lambda works with your existing applications and uses AWS Lambda functions to automatically process and transform your data as it is being retrieved from S3.

5. [Upload to s3 bucket from lambda](https://github.com/amogh9594/aws-with-python/blob/main/aws_lambda/lambda_to_s3.py)
   * Create necessary IAM role our lambda will used.
   * Create s3 bucket.
   * Create json file using Lambda function and upload a json file to s3 bucket.

   

