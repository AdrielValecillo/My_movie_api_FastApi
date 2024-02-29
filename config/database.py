import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = '../database.sqlite'

base_dir = os.path.dirname(os.path.realpath(__file__))

database_URL = 'sqlite:///' + os.path.join(base_dir, sqlite_file_name)


engine = create_engine(database_URL, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

