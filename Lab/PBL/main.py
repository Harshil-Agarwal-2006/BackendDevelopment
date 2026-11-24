import logging
import time
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger("student-api")

app = FastAPI(title="Student API - FastAPI")

students = [
    {"id": 1, "name": "Aarav", "course": "Backend Development"},
    {"id": 2, "name": "Diya", "course": "Backend Development"},
]


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    try:
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "method=%s path=%s status=%s duration_ms=%.2f",
            request.method, request.url.path, response.status_code, duration_ms,
        )
        return response
    except Exception:
        duration_ms = (time.perf_counter() - start) * 1000
        logger.exception(
            "method=%s path=%s status=500 duration_ms=%.2f",
            request.method, request.url.path, duration_ms,
        )
        raise


@app.get("/")
def root():
    return {"application": "Student API", "framework": "FastAPI", "status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/students")
def list_students():
    return students


class Student(BaseModel):
    name: str
    course: str


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students")
def add_student(student: Student):
    new_student = {
        "id": max([s["id"] for s in students], default=0) + 1,
        "name": student.name,
        "course": student.course,
    }

    students.append(new_student)
    return new_student


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for existing_student in students:
        if existing_student["id"] == student_id:
            existing_student["name"] = student.name
            existing_student["course"] = student.course
            return existing_student

    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted"}

    raise HTTPException(status_code=404, detail="Student not found")