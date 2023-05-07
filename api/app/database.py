from sqlalchemy import create_engine
# from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'sqlite:///./course.sqlite3'
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

Base = declarative_base()
