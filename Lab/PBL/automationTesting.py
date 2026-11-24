from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def check(name, condition):
    if condition:
        print(f"[PASS] {name}")
    else:
        print(f"[FAIL] {name}")
        raise AssertionError(f"Test failed: {name}")


# 1. Root
response = client.get("/")
check("GET /", response.status_code == 200)


# 2. Health check
response = client.get("/health")
check(
    "GET /health",
    response.status_code == 200
    and response.json()["status"] == "healthy"
)


# 3. List students
response = client.get("/students")
check(
    "GET /students",
    response.status_code == 200
    and isinstance(response.json(), list)
)


# 4. Create student
response = client.post(
    "/students",
    json={
        "name": "Test Student",
        "course": "Backend Development"
    }
)

check("POST /students", response.status_code == 200)

student_id = response.json()["id"]


# 5. Get created student
response = client.get(f"/students/{student_id}")

check(
    "GET /students/{id}",
    response.status_code == 200
    and response.json()["name"] == "Test Student"
)


# 6. Update student
response = client.put(
    f"/students/{student_id}",
    json={
        "name": "Updated Student",
        "course": "Cloud Computing"
    }
)

check(
    "PUT /students/{id}",
    response.status_code == 200
    and response.json()["name"] == "Updated Student"
)


# 7. Delete student
response = client.delete(f"/students/{student_id}")

check(
    "DELETE /students/{id}",
    response.status_code == 200
)


# 8. Verify deletion
response = client.get(f"/students/{student_id}")

check(
    "GET deleted student returns 404",
    response.status_code == 404
)


print("\nAll automated API tests passed!")