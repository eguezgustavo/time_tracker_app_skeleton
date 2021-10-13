import dataclasses
import datetime
import typing


@dataclasses.dataclass(frozen=True)
class TimeEntry:
    id: int
    google_user_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    customer_id: int
    project_id: int
    activity_id: int
    technologies: typing.List[str]
    ticket: str
    description: str
