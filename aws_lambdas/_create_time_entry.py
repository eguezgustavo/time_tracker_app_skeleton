import datetime
import json

import time_tracker_core
import time_tacker_implementations


def create_time_entry(event, _):
    payload = json.loads(event['body'])

    time_tracker = time_tracker_core.init(
        time_entry_dao=time_tacker_implementations.get_time_entries_dao()
    )
    created_entry = time_tracker.create_a_time_entry(
        google_user_id=payload['googleUserId'],
        start_time=datetime.datetime.strptime(payload['startTime'], '%d/%m/%Y %H:%M'),
        end_time=datetime.datetime.strptime(payload['endTime'], '%d/%m/%Y %H:%M'),
        customer_id=int(payload['customerId']),
        project_id=int(payload['projectId']),
        activity_id=int(payload['activityId']),
        technologies=payload['technologies'],
        ticket=payload['ticket'],
        description=payload['description'],
    )

    response = {
        'statusCode': 200,
        'body': {
            **created_entry.__dict__,
            'start_time': datetime.datetime.strftime(created_entry.start_time, '%d/%m/%Y %H:%M'),
            'end_time': datetime.datetime.strftime(created_entry.end_time, '%d/%m/%Y %H:%M'),
        },
    }

    return json.dumps(response)
