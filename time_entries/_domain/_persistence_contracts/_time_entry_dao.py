import datetime
import typing

from .._entities import TimeEntry


class TimeEntryDao:
    def create(self, time_entry: TimeEntry) -> TimeEntry:
        raise NotImplementedError
