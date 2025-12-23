from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,EmailStr
from datetime import date
app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    email:EmailStr
    dob:date    #YYYY-MM-DD
    gender:str
    degree:str
    college:str

class Student(StudentCreate):
    id: int

# students = {}
students: dict[int, Student] = {}
student_id = 1

@app.get("/students",response_model=list[Student])
def get_all_students():
    return list(students.values())

@app.post("/students",response_model=Student)
def create_student(student: StudentCreate): 
    global student_id
    new_student = Student(id=student_id,**student.model_dump())
    students[student_id] = new_student
    student_id += 1
    return new_student

@app.get("/students/{id}",response_model=Student) 
def get_student(id: int):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[id]

@app.put("/students/{id}",response_model=Student) 
def update_student(id: int,student: StudentCreate): 
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    updated_student = Student(id=id,**student.model_dump())
    students[id] = updated_student
    return updated_student

@app.delete("/students/{id}",response_model=Student) 
def delete_student(id: int):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    return students.pop(id)