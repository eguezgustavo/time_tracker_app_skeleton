from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ._sqlalchemy_base import Base

from time_tracker_core import TimeEntry
from time_tracker_core import TimeEntryDao

from ._sqlalchemy_base import Base

_DATE_FORMAT = '%d/%m/%Y %H:%M'


class _TimeEntryModel(Base):
    __tablename__ = 'time_entries'
    id = Column(Integer, primary_key=True)
    google_user_id = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    customer_id = Column(Integer)
    project_id = Column(Integer)
    activity_id = Column(Integer)
    technologies = Column(String)
    ticket = Column(String)
    description = Column(String)


class TimeEntrySqlalchemyDao(TimeEntryDao):
    def __init__(self, db_connection_string: str):
        _engine = create_engine(db_connection_string, echo=True)
        self.create_session = sessionmaker(bind=_engine)

    def create(self, time_entry: TimeEntry) -> TimeEntry:
        session = self.create_session()
        time_entry_model = _TimeEntryModel(
            google_user_id=time_entry.google_user_id,
            start_time=datetime.strftime(time_entry.start_time, _DATE_FORMAT),
            end_time=datetime.strftime(time_entry.end_time, _DATE_FORMAT),
            customer_id=time_entry.customer_id,
            project_id=time_entry.project_id,
            activity_id=time_entry.activity_id,
            technologies=','.join(time_entry.technologies),
            ticket=time_entry.ticket,
            description=time_entry.description,
        )

        session.add(time_entry_model)
        session.commit()
        session.refresh(time_entry_model)

        return TimeEntry(**{
            **time_entry.__dict__,
            'id': time_entry_model.id,
            }   
        )
