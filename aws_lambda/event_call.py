import json

def lambda_handler(event,context):
    print("Event :", event)
    print("Event is a :", type(event))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    