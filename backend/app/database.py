from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#sqlalchemy is an ORM that can deal with sqlite, mysql, postgresql. We'll use sqlite as the db is in our codebase.
engine = create_engine(
    'sqlite:///./sqlite.db', 
    connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#The above makes database sessions to use everytime we connect to the database

#Instantiate an object called base to make all our tables
Base = declarative_base()


