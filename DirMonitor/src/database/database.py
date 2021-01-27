from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import db_config

user_name = db_config["username"]
password = db_config["password"]
db = db_config["db"]
address = db_config["address"]
schema = db_config["schema"]

engine = create_engine(f"{db}://{user_name}:{password}@{address}/{schema}", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class TaskDetail(Base):
    __tablename__ = "task_detail"
    id = Column(Integer, primary_key=True)
    startTime = Column(DateTime(6))
    endTime = Column(DateTime(6))
    status = Column(String(100))
    configId = Column(Integer)
    magicStringCount = Column(Integer)
    fileList = Column(Text)
    createdAt = Column(DateTime(6))
    updatedAt = Column(DateTime(6))


Base.metadata.create_all(engine)
