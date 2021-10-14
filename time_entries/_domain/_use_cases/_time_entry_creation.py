import datetime
import typing

from .._entities import TimeEntry
from .._services import TimeEntryService


class TimeEntryCreation:
    def __init__(self, service: TimeEntryService) -> None:
        self.service = service
        
    def execute(
        self,
        google_user_id: int,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        customer_id: int,
        project_id: int,
        activity_id: int,
        technologies: typing.List[str],
        ticket: str,
        description: str,
    ) -> TimeEntry:
        return self.service.create(
            TimeEntry(
                id=None,
                google_user_id=google_user_id,
                start_time=start_time,
                end_time=end_time,
                customer_id=customer_id,
                project_id=project_id,
                activity_id=activity_id,
                technologies=technologies,
                ticket=ticket,
                description=description,
            )
        )
