# Experiment 15 – Data Modeling

## Objective

To design and implement data models using SQLAlchemy ORM
and validate API input using Pydantic and FastAPI.

## Concepts Covered

- Conceptual Data Model
- Logical Data Model
- Physical Data Model
- Object Relational Mapping (ORM)
- SQLAlchemy
- Pydantic
- FastAPI
- Primary Keys
- Foreign Keys
- Relationships
- Database Constraints
- Data Validation

## Database Models

### Department

- id
- name

### Student

- id
- name
- email
- branch
- enrollment_date
- department_id

### Course

- id
- title
- credits
- department_id

### Enrollment

- id
- student_id
- course_id
- grade

## Relationships

- Department → Students: 1:M
- Department → Courses: 1:M
- Student → Course: M:N through Enrollment

## Validation

The application validates:

- Student name
- Email format
- Unique email
- Branch
- Enrollment date
- Course credits
- Course grade

Enrollment dates cannot be in the future.

## API

### Create Student

```text
POST /students