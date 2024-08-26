import json
from .test import get_data

def handle(event, ctx):
    # Get data from the other file
    additional_data = get_data()

    # Combine the event data with the additional data
    response_data = {
        "event": event,
        "additional_data": additional_data
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(response_data)
    }

    return response