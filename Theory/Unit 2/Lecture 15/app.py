from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date


app = FastAPI()


# ---------------------------------------------------------
# 1. Pydantic model for incoming student data
# ---------------------------------------------------------
class StudentCreate(BaseModel):
    # Required string.
    # min_length=1 prevents an empty string.
    # max_length=100 prevents excessively long names.
    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    # EmailStr validates that the value has a valid email format.
    email: EmailStr

    # pattern restricts branch to one of the allowed values.
    # Valid: CSE, ECE, IT, ME, CE
    # Invalid: cse, CS, BCA, ABC, etc.
    branch: str = Field(
        ...,
        pattern=r"^(CSE|ECE|IT|ME|CE)$"
    )

    # Optional field.
    # If omitted, its value will be None.
    enrollment_date: Optional[date] = None


# ---------------------------------------------------------
# 2. Pydantic model for API response
# ---------------------------------------------------------
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    branch: str

    # The response expects a date.
    enrollment_date: date


# ---------------------------------------------------------
# 3. Example database model
# ---------------------------------------------------------
# In a real application this would normally be a SQLAlchemy
# model. It is shown here only to complete the example.
class Student:
    _id = 0

    def __init__(
        self,
        name: str,
        email: EmailStr,
        branch: str,
        enrollment_date: Optional[date]
    ):
        Student._id += 1

        self.id = Student._id
        self.name = name
        self.email = email
        self.branch = branch

        # If no enrollment date is supplied, use today's date.
        self.enrollment_date = (
            enrollment_date or date.today()
        )


# ---------------------------------------------------------
# 4. Create endpoint
# ---------------------------------------------------------
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=201
)
def create_student(student: StudentCreate):

    # FastAPI automatically converts the JSON request body
    # into a StudentCreate object.
    #
    # Before this function executes, Pydantic validates:
    #   - name
    #   - email
    #   - branch
    #   - enrollment_date

    # Convert the Pydantic object into a dictionary.
    student_data = student.model_dump()

    # Create the database object.
    db_student = Student(**student_data)

    # Normally we would save it using SQLAlchemy:
    #
    # session.add(db_student)
    # session.commit()
    # session.refresh(db_student)

    return db_student
