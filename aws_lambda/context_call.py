import json

def lambda_handler(event,context):
    print("functionname :", context.function_name)
    print("memory limit in mb :", context.memory_limit_in_mb)
    print("get_remaining_time_in_millis :", context.get_remaining_time_in_millis())
    
    #time.sleep(4)
    
    