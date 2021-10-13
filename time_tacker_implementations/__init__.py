import os

import time_tracker_core
from ._data_access import TimeEntrySqlalchemyDao

_DB_FILE = 'time_tracker.db'


def get_time_entries_dao() -> time_tracker_core.TimeEntryDao:
    environment = os.environ.get('ENV')
    if environment == 'DEV':
        return TimeEntrySqlalchemyDao(f'sqlite:///{_DB_FILE}')
    
    raise NotImplementedError(f'Not implementation for other environment than DEV')
