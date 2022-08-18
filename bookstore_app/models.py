from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    author = Column(String())
    publisher = Column(String())
    publish_date = Column(DateTime())