from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

# Database configuration
DB_NAME = "dev1"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = conn.cursor()

# FastAPI application
app = FastAPI()

# Models
class Teacher(BaseModel):
    id: int
    name: str

class Student(BaseModel):
    id: int
    name: str

# Endpoints
@app.get("/")
def hello_world():
    return "Hello World"

@app.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int):
    cursor.execute("SELECT id, name FROM teachers WHERE id = %s", (teacher_id,))
    result = cursor.fetchone()
    if result:
        teacher = {"id": result[0], "name": result[1]}
        return teacher
    else:
        return {"message": "Teacher not found"}

@app.post("/teachers")
def create_teacher(teacher: Teacher):
    cursor.execute("INSERT INTO teachers (id, name) VALUES (%s, %s)",
                   (teacher.id, teacher.name))
    conn.commit()
    return {"message": "Teacher created"}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    cursor.execute("SELECT id, name FROM students WHERE id = %s", (student_id,))
    result = cursor.fetchone()
    if result:
        student = {"id": result[0], "name": result[1]}
        return student
    else:
        return {"message": "Student not found"}

@app.post("/students")
def create_student(student: Student):
    cursor.execute("INSERT INTO students (id, name) VALUES (%s, %s)",
                   (student.id, student.name))
    conn.commit()
    return {"message": "Student created"}

@app.post("/assign_student")
def assign_student_to_teacher(student_id: int, teacher_id: int):
    cursor.execute("UPDATE students SET teacher_id = %s WHERE id = %s",
                   (teacher_id, student_id))
    conn.commit()
    return {"message": "Student assigned to teacher"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
