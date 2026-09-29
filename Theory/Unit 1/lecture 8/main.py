from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

students = [
    {"id": 1, "name": "Aarav", "branch": "CSE"},
    {"id": 2, "name": "Diya", "branch": "ECE"},
    {"id": 3, "name": "Rohan", "branch": "IT"},
]


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="students.html",
        context={
            "students": students
        }
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )