from pydantic import BaseModel, EmailStr
from datetime import date

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    dob: date          # YYYY-MM-DD
    gender: str
    degree: str
    college: str

class Student(StudentCreate):
    id: int

    class Config:
        from_attributes = True
