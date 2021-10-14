import datetime
import typing

from .._persistence_contracts import TimeEntryDao
from .._entities import TimeEntry


class TimeEntryService:
    def __init__(self, dao: TimeEntryDao) -> None:
        self.dao = dao
    
    def create(self, time_entry: TimeEntry) -> TimeEntry:
        return self.dao.create(time_entry)
