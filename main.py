from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import services, models, schemas
from db import get_db, create_table,engine, Base
app = FastAPI()
create_table()

@app.get("/students", response_model=list[schemas.Student])
def get_all_students(db: Session = Depends(get_db)):
    return services.get_students(db)

@app.post("/students", response_model=schemas.Student)
def create_new_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return services.create_student(db, student)

@app.get("/students/{id}", response_model=schemas.Student)
def get_student_by_id(id: int, db: Session = Depends(get_db)):
    student = services.get_student(db, id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Invalid student ID provided")

@app.put("/students/{id}", response_model=schemas.Student)
def update_student(id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated_student = services.update_student(db, id,student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{id}", response_model=schemas.Student)
def delete_student(id: int, db: Session = Depends(get_db)):
    deleted_student = services.delete_student(db, id)
    if deleted_student:
        return deleted_student
    raise HTTPException(status_code=404, detail="Student not found")