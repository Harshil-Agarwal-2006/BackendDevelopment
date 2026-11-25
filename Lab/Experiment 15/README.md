# Experiment 15 – Django To-Do Management Application

## Overview

This experiment focuses on building a task management web application using the Django framework. The application provides a simple interface through which tasks can be created, viewed, updated, completed, and removed.

Django is used to handle the backend application logic, URL routing, database operations, templates, and administrative functionality. SQLite is used as the database for storing task information.

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS
- JavaScript

## Project Structure

- `manage.py` – Django command-line utility used to manage and run the project.
- `db.sqlite3` – SQLite database containing the application data.
- `todo_project/` – Main Django project configuration directory.
  - `settings.py` – Contains project settings and configuration.
  - `urls.py` – Defines the main project URL configuration.
  - `wsgi.py` – WSGI configuration used for deployment.
  - `asgi.py` – ASGI configuration for asynchronous server support.
- `todo/` – Django application responsible for task management.
  - `models.py` – Defines the database structure for tasks.
  - `views.py` – Contains the logic for processing requests and managing tasks.
  - `urls.py` – Defines application-specific URL routes.
  - `admin.py` – Configures task management through Django Admin.
  - `migrations/` – Stores database migration files.
  - `templates/todo/` – Contains HTML templates used by the application.
  - `static/todo/` – Contains CSS, JavaScript, and image resources.

## Key Features

1. Create new tasks through the web interface.
2. Display stored tasks in a structured task list.
3. Update the completion status of existing tasks.
4. Delete tasks that are no longer required.
5. Store task information persistently using SQLite.
6. Use Django models to represent application data.
7. Render dynamic webpages using Django templates.
8. Reuse common page components through template inheritance and includes.
9. Apply custom styling using static CSS files.
10. Include JavaScript for client-side interface behaviour.
11. Manage task records through the Django Admin interface.
12. Use Django migrations to create and maintain the database structure.

## Concepts Covered

- Django project creation and configuration.
- Django application structure.
- Models and database fields.
- SQLite database integration.
- Database migrations.
- Django views.
- URL routing.
- CRUD-based task management.
- Django Template Language.
- Template inheritance.
- Reusable template components.
- Static files in Django.
- Django Admin configuration.
- Request and response handling.
- Separation of application logic, presentation, and data.

## Learning Outcomes

- Understand the structure of a Django web application.
- Configure and run a Django project using `manage.py`.
- Create models for storing application data.
- Perform database operations using Django's ORM.
- Configure URL patterns and connect them with views.
- Build dynamic pages using Django templates.
- Organize reusable HTML components using template inheritance.
- Integrate CSS and JavaScript as static resources.
- Perform basic CRUD operations in a Django application.
- Use Django Admin to manage database records.
- Understand the role of migrations when modifying database models.

## Conclusion

This experiment provides practical experience in developing a database-driven web application with Django. By implementing a To-Do management system, the experiment demonstrates how Django combines models, views, URL routing, templates, static resources, SQLite, and the Admin interface to create a structured full-stack web application.