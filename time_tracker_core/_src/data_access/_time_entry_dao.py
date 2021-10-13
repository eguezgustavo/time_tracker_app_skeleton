import datetime
import typing

from ..domain_objects import TimeEntry


class TimeEntryDao:
    def create(self, time_entry: TimeEntry) -> TimeEntry:
        raise NotImplementedError
