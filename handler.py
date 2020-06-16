import json
import agnosticcode.Incrementors as a


def validate(event, context):

    jwtToken = event['requestContext']['authorizer']
    print('jwtToken ', jwtToken)

    username = event['requestContext']['authorizer']['claims']['cognito:username']
    print('username ', username)

    print('event', event);

    event_body = json.loads(event['body'])

    inValue = event_body['InValue']
 
    incrementor = a.Incrementors()

    outValue = incrementor.increment(inValue)
    response = {
        'statusCode': 200,
        'body': json.dumps({ 'OutValue': outValue, 'jwtToken': jwtToken, 'username': username })
    }

    return response
