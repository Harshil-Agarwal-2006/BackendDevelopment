# Experiment 12B – Cookies and Session Management using Express.js

## Overview

This experiment demonstrates the implementation of cookies and session management in a Node.js web application using Express.js. It covers creating, retrieving, and deleting cookies, maintaining user-specific session data, tracking user visits, and implementing a simple login and logout mechanism using sessions.

## Technologies Used

- Node.js
- Express.js
- JavaScript
- `cookie-parser`
- `express-session`

## Project Structure

- `package.json` – Contains project information and required dependencies.
- `package-lock.json` – Stores the exact versions of installed npm packages.
- `source/`
  - `cookie-example.js` – Demonstrates creating, retrieving, and deleting cookies.
  - `session-example.js` – Demonstrates session creation, visit tracking, and session destruction.
- `session-cookie-demo/`
  - `server.js` – Combines cookies and sessions to implement a simple login and logout system.
- `README.md` – Project documentation.

## Key Features

1. Create cookies using Express.js.
2. Retrieve stored cookies from client requests.
3. Delete cookies when they are no longer required.
4. Configure cookie expiration using `maxAge`.
5. Create and maintain user sessions using `express-session`.
6. Store information inside a user's session.
7. Track the number of times a user visits a page during a session.
8. Destroy an active session.
9. Implement a simple username-based login system.
10. Maintain login state using session data.
11. Create an additional `theme` cookie after login.
12. Implement logout functionality by destroying the session and clearing the session cookie.
13. Handle HTML form data using Express middleware.
14. Redirect users after login and logout operations.

## Routes Implemented

### Cookie Example

- `GET /` – Confirms that the cookie example server is running.
- `GET /set-cookie` – Creates a `username` cookie.
- `GET /get-cookie` – Retrieves and displays the stored username cookie.
- `GET /delete-cookie` – Deletes the username cookie.

### Session Example

- `GET /` – Creates a session and tracks the number of visits.
- `GET /destroy` – Destroys the current session.

### Session and Cookie Demo

- `GET /` – Displays a login form or welcomes the logged-in user.
- `POST /login` – Stores the username in the session and creates a theme cookie.
- `GET /logout` – Destroys the session, clears the session cookie, and redirects to the home page.

## Concepts Covered

- HTTP cookies.
- Cookie creation and retrieval.
- Cookie deletion.
- Cookie expiration.
- `cookie-parser` middleware.
- Express sessions.
- Session configuration.
- Session cookies.
- Storing server-side session data.
- Session destruction.
- Maintaining user state across requests.
- Basic login and logout functionality.
- Form data handling.
- HTTP redirects.
- Express middleware.
- Request and response handling.

## Learning Outcomes

- Understand the purpose of cookies in web applications.
- Create, access, and remove cookies using Express.js.
- Understand how sessions maintain user-specific state.
- Store and retrieve information using session objects.
- Track user activity across multiple HTTP requests.
- Destroy sessions when they are no longer required.
- Implement basic login and logout functionality using sessions.
- Understand the relationship between browser cookies and server-side sessions.
- Configure cookie expiration and session behavior.
- Use Express middleware for cookies, sessions, and form processing.

## Conclusion

This experiment demonstrates state management in Express.js applications using cookies and sessions. It provides practical experience with storing client-side cookie information, maintaining server-side session data, tracking user activity, and implementing a basic login and logout workflow. These concepts form the foundation for authentication and user-state management in backend web applications.