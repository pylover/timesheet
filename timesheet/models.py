# -*- coding: utf-8 -*-
__author__ = 'vahid'


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy import create_engine, Column, DateTime, String, Integer, ForeignKey
from datetime import datetime
from timesheet import config

maker = sessionmaker()
DBSession = scoped_session(maker)
BaseModel = declarative_base()
BaseModel.query = DBSession.query_property()
metadata = BaseModel.metadata


class Subject(BaseModel):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, index=True, unique=True)
    entry_time = Column(DateTime, nullable=False, default=datetime.now)

    @classmethod
    def ensure(cls, title):
        s = cls.query.filter(cls.title == title).first()
        if not s:
            s = cls(title=title)
            DBSession.add(s)
        return s

    def __repr__(self):
        return '<%s created=%s >' % (
            self.title,
            self.entry_time.strftime(config.datetime_format)
        )


class Task(BaseModel):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=True)
    start_time = Column(DateTime, nullable=False, default=datetime.now)
    end_time = Column(DateTime, nullable=True)
    subject_id = Column(Integer, ForeignKey('subject.id'))

    subject = relationship("Subject", backref=backref('tasks', order_by=start_time))

    @classmethod
    def get_active_task(cls):
        task = cls.query.filter(cls.end_time == None).order_by(cls.start_time.desc()).first()
        return task

    @classmethod
    def get_last_task(cls):
        task = cls.query.order_by(cls.end_time.desc()).first()
        return task

    def end(self):
        self.end_time = datetime.now()

    @property
    def hours(self):
        if not self.end_time:
            return 0
        else:
            return (self.end_time - self.start_time).total_seconds() / 3600.0

    def __repr__(self):
        return '<Subject=%s title=%s start=%s end=%s>' % (
            self.subject.title,
            self.title,
            self.start_time_string,
            self.end_time_string
        )

    @property
    def start_time_string(self):
        return self.start_time.strftime(config.datetime_format)

    @property
    def end_time_string(self):
        return '' if not self.end_time else self.end_time.strftime(config.datetime_format)


def init():
    engine = create_engine(config.db.uri, echo=config.db.echo)
    DBSession.configure(bind=engine)
    BaseModel.metadata.create_all(engine)
