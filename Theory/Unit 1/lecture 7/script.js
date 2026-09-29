let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

// Display tasks when page loads
displayTasks();

function addTask() {
    let input = document.getElementById("taskInput");
    let task = input.value.trim();

    if (task === "") {
        alert("Please enter a task");
        return;
    }

    tasks.push(task);

    // Store permanently using localStorage
    localStorage.setItem("tasks", JSON.stringify(tasks));

    // Store current session information
    sessionStorage.setItem("lastTask", task);

    input.value = "";

    displayTasks();
}

function displayTasks() {
    let list = document.getElementById("taskList");
    list.innerHTML = "";

    tasks.forEach(function(task, index) {
        let li = document.createElement("li");

        li.innerHTML = `
            ${task}
            <button onclick="deleteTask(${index})">Delete</button>
        `;

        list.appendChild(li);
    });
}

function deleteTask(index) {
    tasks.splice(index, 1);

    localStorage.setItem("tasks", JSON.stringify(tasks));

    displayTasks();
}

function clearTasks() {
    tasks = [];

    localStorage.removeItem("tasks");
    sessionStorage.removeItem("lastTask");

    displayTasks();
}