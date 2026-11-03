from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str

students = {
    1: "Aman",
    2: "Riya",
    3: "Karan"
}

@app.get("/hello")
def hello():
    return {"message": "hello Chirag"}

@app.get("/bye")
def bye():
    return {"message": "bye Chirag"}

@app.get("/students/{roll_no}")
def get_student(roll_no: int):
    if roll_no in students:
        return {"name": students[roll_no]}
    raise HTTPException(status_code = 404, detail = "student not found")

@app.post("/students")
def create_student(student: Student):
    new_id = len(students) + 1
    students[new_id] = student.name
    return {"id": new_id, "name": student.name}

