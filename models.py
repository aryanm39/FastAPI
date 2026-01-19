from db import Base
from sqlalchemy import Column, Integer, String,TEXT

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")

class Blog(Base):
    __tablename__='blogs'
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    body=Column(TEXT)
    author=Column(String)
    
