import datetime
import typing

from ..data_access import TimeEntryDao
from ..domain_objects import TimeEntry


class TimeEntryService:
    def __init__(self, dao: TimeEntryDao) -> None:
        self.dao = dao
    
    def create(self, time_entry: TimeEntry) -> TimeEntry:
        return self.dao.create(time_entry)
