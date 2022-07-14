import boto3
from datetime import date
# aws_connection = boto3.session.Session(profile_name="profile_name")
# cloudwatch = aws_connection.client('logs')

#Log stream search as per date.
today = date.today()
d1 = today.strftime("%Y/%m/%d")
print(type(d1))

AWS_REGION = "xxxxxxxxxxxxxxxx"
cloudwatch = boto3.client('logs', region_name=AWS_REGION,aws_access_key_id="xxxxxxxxxxxxxx",aws_secret_access_key="xxxxxxxxxxxxxxxxxx")


log_group_to_scan="xxxxxxxxxxxxxx"
log_stream_filter_prefix="xxxxxxxxxxxxxxxxxxxxxx"
print(type(log_stream_filter_prefix))


try:

    response = cloudwatch.describe_log_streams(logGroupName=log_group_to_scan, 
                                               descending=True, 
                                               logStreamNamePrefix=d1
                                               )
   
    for logstream in response["logStreams"]:

        logstream_name = logstream["logStreamName"]
        print(f"Extracting logs for stream {logstream_name}")

        log_details = cloudwatch.get_log_events(
            logGroupName=log_group_to_scan,
            logStreamName=logstream_name,
        )

        for event in log_details["events"]:
            timestamp = int(event["timestamp"])
            message = str(event["message"])
            log = (f"{timestamp}:{message}")
            print(log)

except Exception as e:
	print(e)