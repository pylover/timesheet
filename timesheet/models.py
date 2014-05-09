# -*- coding: utf-8 -*-
__author__ = 'vahid'


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, Column, DateTime, String, Integer
from datetime import datetime

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


class Timesheet(BaseModel):
    __tablename__ = 'timesheet'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=True)
    start_time = Column(DateTime, nullable=False, default=datetime.now)
    end_time = Column(DateTime, nullable=True)


def init():
    from timesheet import config
    engine = create_engine(config.db.uri, echo=config.db.echo)
    DBSession.configure(bind=engine)
    BaseModel.metadata.create_all(engine)

