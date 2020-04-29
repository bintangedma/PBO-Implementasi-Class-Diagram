from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///Visitor.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
print(Session)