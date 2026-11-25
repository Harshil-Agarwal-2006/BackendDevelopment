# Mid-Sem Lab Test – Todo Matrix

## Overview

This project implements a Todo Matrix web application for organizing tasks according to their **importance** and **urgency**. Tasks are automatically classified into four different quadrants, helping users determine which tasks should be completed first, scheduled, delegated, or avoided.

The backend is developed using Flask, while MongoDB is used to permanently store task information. The frontend communicates with the Flask REST API using JavaScript Fetch API requests.

## Technologies Used

- Python
- Flask
- MongoDB
- PyMongo
- HTML5
- CSS
- JavaScript
- Fetch API

## Project Structure

- `app.py` – Main Flask application containing database configuration and API routes.
- `requirements.txt` – Contains the required Python packages.
- `templates/`
  - `index.html` – Main user interface for adding and viewing tasks.
- `static/`
  - `style.css` – Contains styling for the Todo Matrix interface.
  - `script.js` – Handles API communication, task rendering, addition, and deletion.
- `README.md` – Basic project documentation.

## Key Features

1. Add new tasks through a web-based form.
2. Assign an importance value to each task.
3. Assign an urgency value to each task.
4. Automatically classify tasks into four matrix quadrants.
5. Store task information persistently in MongoDB.
6. Retrieve all stored tasks through a REST API.
7. Dynamically display tasks without reloading the webpage.
8. Delete tasks directly from their respective quadrants.
9. Validate task information before storing it.
10. Handle invalid task IDs and missing tasks using appropriate HTTP responses.

## Todo Matrix Classification

Tasks are classified according to their importance and urgency values:

- **Q1 – Important & Urgent:** Tasks that should be completed first.
- **Q2 – Important & Not Urgent:** Tasks that should be planned or scheduled.
- **Q3 – Not Important & Urgent:** Tasks that can be delegated or completed quickly.
- **Q4 – Not Important & Not Urgent:** Tasks that can be avoided or eliminated.

## API Endpoints

- `GET /` – Renders the Todo Matrix webpage.
- `GET /api/tasks` – Retrieves all tasks stored in MongoDB.
- `POST /api/tasks` – Creates and stores a new task.
- `DELETE /api/tasks/<task_id>` – Deletes a specific task using its MongoDB ObjectId.

## Data Model

Each task stored in MongoDB contains:

- `title` – Name or description of the task.
- `importance` – Indicates whether the task is important (`1`) or not important (`0`).
- `urgency` – Indicates whether the task is urgent (`1`) or not urgent (`0`).

MongoDB automatically generates a unique `_id` for every task.

## Concepts Covered

- Flask application development.
- REST API creation.
- MongoDB database integration.
- PyMongo database operations.
- MongoDB ObjectId handling.
- HTTP GET, POST, and DELETE methods.
- JSON request and response handling.
- Input validation and error handling.
- HTTP status codes.
- JavaScript Fetch API.
- Asynchronous JavaScript using `async` and `await`.
- DOM manipulation.
- Event handling.
- Dynamic content rendering.
- Client-server communication.
- Task classification using conditional logic.

## Learning Outcomes

- Develop a full-stack web application using Flask.
- Connect a Python backend application with MongoDB.
- Create REST API endpoints for managing application data.
- Perform insert, retrieve, and delete operations using PyMongo.
- Validate incoming API data and return appropriate HTTP status codes.
- Communicate with backend APIs using the JavaScript Fetch API.
- Dynamically update webpage content using DOM manipulation.
- Organize tasks using an importance-versus-urgency matrix.
- Understand interaction between the frontend, backend, and database layers.

## Conclusion

The Mid-Sem Lab Test demonstrates the development of a full-stack Todo Matrix application using Flask and MongoDB. The project combines REST APIs, persistent database storage, asynchronous frontend requests, and dynamic DOM manipulation to provide a practical task-management system based on importance and urgency.