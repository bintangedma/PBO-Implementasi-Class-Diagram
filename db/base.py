from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///Hotel.db')

Session = sessionmaker(bind=engine)

def sessionFactory():
    Base.metadata.create_all(engine)
    return Session()