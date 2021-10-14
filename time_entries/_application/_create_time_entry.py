import datetime
import json

from .._domain import TimeEntryCreation
from .._domain import TimeEntryService
from .._infrastructure import TimeEntrySqlalchemyDao


def create_time_entry(event, _):
    payload = json.loads(event['body'])
    dao = TimeEntrySqlalchemyDao('sqlite:///fake.db')
    service = TimeEntryService(dao)
    time_entry_creation = TimeEntryCreation(service)

    created_entry = time_entry_creation.execute(
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
