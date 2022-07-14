import boto3

AWS_REGION = "xxxxxxxxx"

client = boto3.client('logs', region_name=AWS_REGION,aws_access_key_id="xxxxxxxxxxxxxxx",aws_secret_access_key="xxxxxxxxxxxxxxxx")

#messages = ["new logstream created."]

response = client.create_log_stream(
    logGroupName='xxxxxxxxxxxxxxxxx',
    logStreamName='xxxxxxxxxxxxxxxx'
)

seq_token = None

for i in range(10):
    log_event = {
        'logGroupName': 'xxxxxxxxxxxxxxxxx',
        'logStreamName': 'xxxxxxxxxxxxxxxx',
        'logEvents': [
            {
                'timestamp': int(round(time.time() * 1000)),
                'message': "new logstream created."
            },
        ],
    }

    if seq_token:
        log_event['sequenceToken'] = seq_token

    response = client.put_log_events(**log_event)

    seq_token = response['nextSequenceToken']
    time.sleep(1)

print("Logs generated successfully")