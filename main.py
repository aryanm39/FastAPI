from fastapi import FastAPI, HTTPException
app = FastAPI()

students = {}
student_id = 1

@app.get("/students") 
def get_all():
    return list(students.values())

@app.post("/students")
def create_student(student: dict):
    global student_id
    student["id"] = student_id
    students[student_id] = student
    student_id += 1
    return student

@app.get("/students/{id}") 
def get_student(id: int):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[id]

@app.put("/students/{id}") 
def update_student(id: int, student: dict):  
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    student["id"] = id
    students[id] = student
    return student

@app.delete("/students/{id}")
def delete_student(id: int):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    return students.pop(id)