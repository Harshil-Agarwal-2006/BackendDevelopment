// =========================================
// GET ELEMENTS FROM HTML
// =========================================

const taskForm = document.getElementById("taskForm");

const titleInput = document.getElementById("title");

const importanceInput = document.getElementById("importance");

const urgencyInput = document.getElementById("urgency");


// Get the four quadrants

const quadrant1 = document.querySelector("#quadrant1 .task-container");

const quadrant2 = document.querySelector("#quadrant2 .task-container");

const quadrant3 = document.querySelector("#quadrant3 .task-container");

const quadrant4 = document.querySelector("#quadrant4 .task-container");


// =========================================
// LOAD TASKS FROM FLASK
// =========================================

async function loadTasks() {

    try {

        const response = await fetch("/api/tasks");

        const tasks = await response.json();


        // Clear existing tasks

        quadrant1.innerHTML = "";

        quadrant2.innerHTML = "";

        quadrant3.innerHTML = "";

        quadrant4.innerHTML = "";


        // Put every task in its correct quadrant

        tasks.forEach(task => {

            addTaskToQuadrant(task);

        });

    }

    catch (error) {

        console.error("Error loading tasks:", error);

    }

}


// =========================================
// DETERMINE QUADRANT
// =========================================

function addTaskToQuadrant(task) {

    let targetQuadrant;


    /*
        Importance = 1
        Urgency = 1
        → Q1
    */

    if (task.importance === 1 && task.urgency === 1) {

        targetQuadrant = quadrant1;

    }


    /*
        Importance = 1
        Urgency = 0
        → Q2
    */

    else if (task.importance === 1 && task.urgency === 0) {

        targetQuadrant = quadrant2;

    }


    /*
        Importance = 0
        Urgency = 1
        → Q3
    */

    else if (task.importance === 0 && task.urgency === 1) {

        targetQuadrant = quadrant3;

    }


    /*
        Importance = 0
        Urgency = 0
        → Q4
    */

    else {

        targetQuadrant = quadrant4;

    }


    // Create the task card

    const taskCard = createTaskCard(task);


    // Put the card inside the correct quadrant

    targetQuadrant.appendChild(taskCard);

}


// =========================================
// CREATE TASK CARD
// =========================================

function createTaskCard(task) {

    // Create the main card

    const card = document.createElement("div");

    card.classList.add("task-card");


    // =====================================
    // TASK TITLE
    // =====================================

    const title = document.createElement("div");

    title.classList.add("task-title");

    title.textContent = task.title;


    // =====================================
    // TASK INFORMATION
    // =====================================

    const info = document.createElement("div");

    info.classList.add("task-info");

    info.textContent =
        "Importance: " +
        task.importance +
        " | Urgency: " +
        task.urgency;


    // =====================================
    // DELETE BUTTON
    // =====================================

    const deleteButton = document.createElement("button");

    deleteButton.classList.add("delete-button");

    deleteButton.textContent = "Delete";


    // When the button is clicked

    deleteButton.addEventListener("click", function () {

        deleteTask(task.id);

    });


    // =====================================
    // ADD EVERYTHING TO CARD
    // =====================================

    card.appendChild(title);

    card.appendChild(info);

    card.appendChild(deleteButton);


    return card;

}


// =========================================
// ADD NEW TASK
// =========================================

taskForm.addEventListener("submit", async function (event) {

    // Stop the page from refreshing

    event.preventDefault();


    // Get values from form

    const title = titleInput.value.trim();

    const importance = Number(importanceInput.value);

    const urgency = Number(urgencyInput.value);


    // Make sure title isn't empty

    if (title === "") {

        alert("Please enter a task.");

        return;

    }


    try {

        // Send task to Flask

        const response = await fetch("/api/tasks", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                title: title,

                importance: importance,

                urgency: urgency

            })

        });


        const data = await response.json();


        // Check for errors

        if (!response.ok) {

            alert(data.error);

            return;

        }


        // Clear form

        taskForm.reset();


        // Reload tasks

        loadTasks();

    }

    catch (error) {

        console.error("Error adding task:", error);

        alert("Could not add task.");

    }

});


// =========================================
// DELETE TASK
// =========================================

async function deleteTask(taskId) {

    try {

        const response = await fetch(
            `/api/tasks/${taskId}`,
            {
                method: "DELETE"
            }
        );


        const data = await response.json();


        if (!response.ok) {

            alert(data.error);

            return;

        }


        // Reload tasks after deletion

        loadTasks();

    }

    catch (error) {

        console.error("Error deleting task:", error);

    }

}


// =========================================
// LOAD TASKS WHEN PAGE OPENS
// =========================================

loadTasks();