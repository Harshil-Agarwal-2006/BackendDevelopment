from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date

# Create database connection
engine = create_engine("sqlite:///students.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# --- Models with back_populates ---
# 'back_populates' creates a bidirectional relationship. 
# It links the 'Student' object to the 'Department' object and vice-versa.
# For example, if you have a 'Student' object, you can access their 'department' 
# object directly (student.department). Conversely, if you have a 'Department' 
# object, you can access all 'students' belonging to that department 
# (department.students). SQLAlchemy manages the synchronization automatically 
# when you update either side of the relationship.

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    
    # The relationship tells SQLAlchemy how to link Department to Student.
    # When you query a department, you can immediately access all associated students.
    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    branch = Column(String(50))
    enrollment_date = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    # The relationship tells SQLAlchemy how to link Student back to Department.
    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(String(10), primary_key=True)
    title = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")

class Enrollment(Base):
    __tablename__ = "enrollments"
    
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(String(10), ForeignKey("courses.id"), primary_key=True)
    semester = Column(String(20))
    grade = Column(String(2))
    
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")



# Create tables
Base.metadata.create_all(engine)

# --- CRUD Operations ---

# CREATE: Adding new data
print("\n--- CREATE ---")
new_student = Student(
    name="Aarav",
    email="Aarav@upes.ac.in",  # Changed to be unique
    branch="CSE",
    enrollment_date=date(2024, 8, 1),
    department_id=1  # Ensure this department ID exists in departments table
)
session.add(new_student)
# session.commit() is essential. Without it, the changes remain in memory 
# and are not written to the 'students.db' file.
session.commit()
print("Student added and committed to the database.")

# READ: Retrieving data
print("\n--- READ ---")
students = session.query(Student).filter(Student.branch == "CSE").all()
# Fetching the first student to demonstrate
student = session.query(Student).filter_by(id=1).first()

print(f"Retrieved student (ID 1): {student.name if student else 'Not Found'}")
print(f"Retrieved all CSE students: {[s.name for s in students]}")

# UPDATE: Modifying data
print("\n--- UPDATE ---")
if student:
    # Modify the object in memory
    student.branch = "ECE"
    # Commit to persist the change in the database file
    session.commit()
    print(f"Student {student.name} branch updated to ECE in the database.")

# DELETE: Removing data
print("\n--- DELETE ---")
# Let's delete the student we just created (assuming it's the one with id=2 or similar)
# We need to find the student first
student_to_delete = session.query(Student).filter_by(name="Aarav").first()
if student_to_delete:
    session.delete(student_to_delete)
    # Commit to finalize the deletion in the database file
    session.commit()
    print("Student 'Aarav' deleted from the database.")
else:
    print("Student 'Aarav' not found for deletion.")

