# Assignment 01 – Notes App using LocalStorage

## Overview

This assignment involves developing a simple Notes Application using HTML, CSS, and JavaScript. The application allows users to create, view, edit, and delete notes directly in the browser.

The notes are stored using the browser's `localStorage`, allowing the data to remain available even after the page is refreshed or reopened.

## Technologies Used

- HTML5
- CSS
- JavaScript
- LocalStorage
- JSON

## Project Structure

- `index.html` – Contains the structure and user interface of the Notes App.
- `style.css` – Provides styling for the application and individual notes.
- `script.js` – Contains the application logic for creating, displaying, editing, deleting, and storing notes.
- `README.md` – Contains documentation for the assignment.

## Key Features

1. Add new notes through a text input area.
2. Display all saved notes on the webpage.
3. Edit existing notes.
4. Delete notes that are no longer required.
5. Store notes permanently using browser `localStorage`.
6. Automatically restore saved notes when the page is loaded again.
7. Store creation and modification timestamps for each note.
8. Display the last updated time for saved notes.
9. Validate note input to prevent empty notes.
10. Dynamically update the user interface without reloading the page.

## Note Structure

Each note is represented as a JavaScript object containing:

- `id` – Unique identifier generated using `Date.now()`.
- `text` – Content entered by the user.
- `createdAt` – Date and time when the note was created.
- `updatedAt` – Date and time when the note was last modified.

Example:

```javascript
{
    id: 1764060000000,
    text: "Complete Backend Assignment",
    createdAt: "2026-11-25T10:00:00.000Z",
    updatedAt: "2026-11-25T10:00:00.000Z"
}
```

## LocalStorage Implementation

Since `localStorage` stores data as strings, JavaScript objects and arrays are converted to JSON before being stored:

```javascript
localStorage.setItem("notes", JSON.stringify(notes));
```

The stored JSON is converted back into JavaScript data when retrieved:

```javascript
JSON.parse(localStorage.getItem("notes"));
```

This allows the notes to persist even after refreshing or reopening the webpage.

## Operations Implemented

### Add Note

The application reads the note entered by the user, creates a new note object, and stores it in `localStorage`.

### Display Notes

Saved notes are retrieved from `localStorage` and dynamically displayed on the webpage.

### Edit Note

Users can modify the text of an existing note. The `updatedAt` timestamp is updated whenever a note is edited.

### Delete Note

Users can remove a note from the notes array, after which the updated array is saved back to `localStorage`.

## Concepts Covered

- Browser LocalStorage.
- JSON serialization and deserialization.
- JavaScript objects and arrays.
- DOM manipulation.
- Event listeners.
- Dynamic HTML element creation.
- Array methods such as `find()` and `filter()`.
- JavaScript functions.
- Input validation.
- Date and time handling.
- Persistent client-side storage.
- CRUD operations.

## Learning Outcomes

- Understand how browser `localStorage` can be used for persistent data storage.
- Store JavaScript objects and arrays using JSON.
- Retrieve and parse stored JSON data.
- Implement create, read, update, and delete operations.
- Dynamically manipulate webpage content using JavaScript.
- Handle user interactions using event listeners.
- Maintain application data after browser refreshes.
- Build a complete client-side application without requiring a backend database.

## Conclusion

This assignment demonstrates the development of a browser-based Notes Application using JavaScript and `localStorage`. It implements complete CRUD functionality while using JSON to persist structured note data between browser sessions. The project provides practical experience with DOM manipulation, event handling, JSON, and client-side data persistence.