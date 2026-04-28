
from sqlalchemy import Column, Integer, String, Date
from db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    dob = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    college = Column(String, nullable=False)
