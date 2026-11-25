const noteInput = document.getElementById("noteInput");
const addNoteBtn = document.getElementById("addNoteBtn");
const notesContainer = document.getElementById("notesContainer");


// Get notes from localStorage
function getNotes() {
    const notes = localStorage.getItem("notes");

    if (notes) {
        return JSON.parse(notes);
    }

    return [];
}


// Save notes to localStorage
function saveNotes(notes) {
    localStorage.setItem("notes", JSON.stringify(notes));
}


// Display all notes
function displayNotes() {
    const notes = getNotes();

    notesContainer.innerHTML = "";

    if (notes.length === 0) {
        notesContainer.innerHTML =
            '<p class="empty-message">No notes yet. Add your first note!</p>';
        return;
    }

    notes.forEach((note) => {
        const noteElement = document.createElement("div");
        noteElement.classList.add("note");

        const text = document.createElement("p");
        text.textContent = note.text;

        const date = document.createElement("small");
        date.textContent =
            "Last updated: " +
            new Date(note.updatedAt).toLocaleString();

        const actions = document.createElement("div");
        actions.classList.add("note-actions");

        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.classList.add("edit-btn");
        editButton.addEventListener("click", () => {
            editNote(note.id);
        });

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.classList.add("delete-btn");
        deleteButton.addEventListener("click", () => {
            deleteNote(note.id);
        });

        actions.appendChild(editButton);
        actions.appendChild(deleteButton);

        noteElement.appendChild(text);
        noteElement.appendChild(date);
        noteElement.appendChild(actions);

        notesContainer.appendChild(noteElement);
    });
}


// Add a new note
function addNote() {
    const text = noteInput.value.trim();

    if (text === "") {
        alert("Please enter a note.");
        return;
    }

    const notes = getNotes();

    const newNote = {
        id: Date.now(),
        text: text,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString()
    };

    notes.push(newNote);

    saveNotes(notes);

    noteInput.value = "";

    displayNotes();
}


// Edit an existing note
function editNote(id) {
    const notes = getNotes();

    const note = notes.find((note) => note.id === id);

    if (!note) {
        return;
    }

    const updatedText = prompt("Edit your note:", note.text);

    if (updatedText === null) {
        return;
    }

    if (updatedText.trim() === "") {
        alert("Note cannot be empty.");
        return;
    }

    note.text = updatedText.trim();
    note.updatedAt = new Date().toISOString();

    saveNotes(notes);

    displayNotes();
}


// Delete a note
function deleteNote(id) {
    const notes = getNotes();

    const updatedNotes = notes.filter((note) => note.id !== id);

    saveNotes(updatedNotes);

    displayNotes();
}


// Add note when button is clicked
addNoteBtn.addEventListener("click", addNote);


// Display saved notes when page loads
displayNotes();