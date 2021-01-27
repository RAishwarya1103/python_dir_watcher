from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://dirWatcher:DirWatch@123@localhost:3306/dirwatch_python", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Configuration(Base):
    __tablename__ = "configuration"
    id = Column(Integer, primary_key=True)
    directory = Column(String(100))
    magicString = Column(String(100))
    isActive = Column(Boolean)
    createdAt = Column(DateTime(6))
    updatedAt = Column(DateTime(6))


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
