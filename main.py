from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.middleware(
    CORSMiddleware:
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )




class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1, name="John Doe", grade=95),
    Student(id=2, name="Jane Smith", grade=88),
    Student(id=3, name="Alice Johnson", grade=92),
    Student(id=4, name="Bob Brown", grade=85),
    Student(id=5, name="Charlie Wilson", grade=97),
]

@app.get("/students")
def get_students():
    return students


@app.post("/students")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
        return {"error": "Student not found"}
    

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted successfully"}
    return {"error": "Student not found"}