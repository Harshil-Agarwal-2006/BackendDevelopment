# Experiment 12A – Node.js, Express.js and EJS

## Overview

This experiment demonstrates backend web development using Node.js and Express.js. It covers the creation of an Express server, different types of HTTP responses, route parameters, query parameters, POST requests, basic authentication logic, and dynamic webpage rendering using EJS templates.

## Technologies Used

- Node.js
- Express.js
- EJS
- JavaScript
- HTML
- CSS
- Nodemon

## Project Structure

- `app.js` – Main Express server containing routes and application logic.
- `script.js` – Basic Node.js script demonstrating console output, variables, arrays, and array operations.
- `package.json` – Project configuration containing dependencies and npm scripts.
- `package-lock.json` – Stores exact versions of installed npm packages.
- `views/` – Contains EJS templates used for dynamic webpage rendering.
  - `home.ejs` – Dynamic home page.
  - `users.ejs` – Displays a list of users in tabular form.
  - `profile.ejs` – Displays individual user profile information.
- `README.md` – Experiment documentation.

## Key Features

1. Create and run an Express.js web server.
2. Handle multiple GET and POST routes.
3. Return plain text responses from the server.
4. Return HTML content through Express routes.
5. Return structured JSON responses.
6. Access dynamic route parameters using `/user/:id`.
7. Process query parameters for search operations.
8. Perform basic arithmetic calculations using query parameters.
9. Handle user registration data through a POST request.
10. Implement basic login validation with success and unauthorized responses.
11. Render dynamic webpages using EJS.
12. Display user information dynamically using EJS templates.
13. Render a collection of users in an HTML table.
14. Use URL-encoded and JSON request body parsing.

## Routes Implemented

- `GET /` – Displays the Express server welcome message.
- `GET /text` – Returns a plain text response.
- `GET /html` – Returns HTML content.
- `GET /json` – Returns structured JSON data.
- `GET /user/:id` – Retrieves a user ID through a route parameter.
- `GET /search` – Processes search, page, and limit query parameters.
- `GET /calculate` – Performs arithmetic operations using query parameters.
- `POST /register` – Processes user registration information.
- `POST /login` – Performs basic login credential validation.
- `GET /home` – Renders the EJS home page.
- `GET /users` – Renders a list of users using EJS.
- `GET /profile/:id` – Renders user profile information using EJS.

## Concepts Covered

- Node.js runtime environment.
- Express.js application setup.
- HTTP GET and POST methods.
- Express routing.
- Route parameters.
- Query parameters.
- Request body handling.
- JSON and URL-encoded middleware.
- HTTP status codes.
- JSON, HTML, and text responses.
- Basic