from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    complete = Column(Boolean, default=False) 
