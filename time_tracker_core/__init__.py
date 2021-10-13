from ._src.data_access import TimeEntryDao
from ._src.domain_objects import TimeEntry
from ._src.services import TimeEntryService
from ._use_cases import TimeEntryFunctionalities


class TimeTracker:
    def __init__(self, time_entry_functionalities: TimeEntryFunctionalities) -> None:
        self.create_a_time_entry = time_entry_functionalities.create_a_time_entry


def init(time_entry_dao: TimeEntryDao) -> TimeTracker:
    return TimeTracker(
        time_entry_functionalities=TimeEntryFunctionalities(
            service=TimeEntryService(
                dao=time_entry_dao,
            )
        )
    )
