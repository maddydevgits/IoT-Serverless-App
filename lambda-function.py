import json
import urllib3
http = urllib3.PoolManager()

cloudapi='https://api.thingspeak.com/update?api_key=94RKOKI1H4EFY6CL&field1='
def lambda_handler(event, context):
    # TODO implement
    k=event['body']
    k=k.split(':')
    k=k[-1]
    k=k.split('\'')
    k=k[1]
    k=k
    print(k)
    if(k=='on'):
        while True:
            response = http.request("GET", cloudapi+'1')
            print(response)
            if(response!=0):
                break
    elif (k=='off'):
        while True:
            response=http.request('GET',cloudapi+'0')
            if(response!=0):
                break
            
    return {
        'statusCode': 200,
        'body': json.dumps(k)
    }
