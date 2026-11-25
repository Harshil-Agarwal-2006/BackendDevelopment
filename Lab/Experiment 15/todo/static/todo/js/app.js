
document.addEventListener('DOMContentLoaded', function () {
    // Automatically focus the task title input on the Add Task page
    const titleInput = document.getElementById('title');

    if (titleInput) {
        titleInput.focus();
    }

    console.log('Task Tracker application loaded successfully.');
});
