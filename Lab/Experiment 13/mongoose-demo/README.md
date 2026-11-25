# Experiment 13 – MongoDB and Mongoose User Management System

## Overview

This experiment involves developing a simple User Management System using Node.js, Express.js, MongoDB, and Mongoose. The application connects an Express server to a MongoDB database and demonstrates how user information can be stored, retrieved, and validated using a Mongoose schema and model.

The application provides functionality for user registration, login, and displaying all registered users.

## Technologies Used

- Node.js
- Express.js
- MongoDB
- Mongoose
- JavaScript
- HTML
- CSS
- dotenv

## Project Structure

- `mongoose-demo/` – Main project directory.
- `server.js` – Main Express server containing MongoDB connection, Mongoose schema, model, routes, and application logic.
- `package.json` – Contains project information and required dependencies.
- `package-lock.json` – Stores exact versions of installed npm packages.
- `.gitignore` – Specifies files and folders that should not be tracked by Git.
- `README.md` – Project documentation.

## Key Features

1. Connect an Express.js application to MongoDB using Mongoose.
2. Configure the MongoDB connection using an environment variable.
3. Define a Mongoose schema for storing user information.
4. Create a Mongoose model for interacting with the users collection.
5. Register new users using a signup form.
6. Store username, email, password, and account creation date in MongoDB.
7. Ensure usernames and email addresses are unique.
8. Validate required user fields through the Mongoose schema.
9. Implement user login by retrieving user information from MongoDB.
10. Check submitted login credentials against stored user data.
11. Display all registered users stored in the database.
12. Handle duplicate usernames and email addresses.
13. Parse JSON and URL-encoded request data using Express middleware.
14. Provide a simple HTML and CSS interface for interacting with the application.

## Routes Implemented

- `GET /` – Displays the User Management System home page containing registration, login, and user listing options.
- `POST /signup` – Creates and stores a new user in MongoDB.
- `POST /login` – Finds a user by username and validates the submitted password.
- `GET /users` – Retrieves and displays all registered users from MongoDB.

## Mongoose Schema

The application defines a user schema containing the following fields:

- `username` – Required and unique username.
- `email` – Required and unique email address.
- `password` – Required user password.
- `createdAt` – Stores the account creation date and automatically defaults to the current date and time.

## Concepts Covered

- MongoDB database integration.
- Mongoose Object Data Modeling (ODM).
- Connecting Node.js applications to MongoDB.
- Environment variables using `dotenv`.
- Mongoose schemas and models.
- Creating and saving MongoDB documents.
- Retrieving documents using `find()` and `findOne()`.
- Schema validation.
- Unique database fields.
- Asynchronous database operations using `async` and `await`.
- Express.js routing.
- GET and POST requests.
- Form data handling.
- JSON and URL-encoded middleware.
- Error handling using `try` and `catch`.
- Handling duplicate database entries.
- Dynamic HTML responses.

## Learning Outcomes

- Understand how MongoDB can be integrated with a Node.js application.
- Connect an Express.js server to MongoDB using Mongoose.
- Create schemas and models for structured database operations.
- Insert and retrieve documents from a MongoDB collection.
- Implement basic user registration functionality.
- Retrieve user information for login validation.
- Handle asynchronous database operations using `async` and `await`.
- Use environment variables for database configuration.
- Handle database validation and duplicate entry errors.
- Build a simple database-driven web application using Express and MongoDB.

## Conclusion

This experiment demonstrates database integration in a Node.js and Express.js application using MongoDB and Mongoose. It covers database connectivity, schema and model creation, user registration, login validation, data retrieval, and error handling. The experiment provides practical experience with building a basic database-driven User Management System.