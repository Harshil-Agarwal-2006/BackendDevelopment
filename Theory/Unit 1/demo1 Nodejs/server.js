const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Welcome to the Student Management API");
});

app.get("/students", (req, res) => {
    res.send("List of all students");
});

app.get("/students/1", (req, res) => {
    res.send("Student: Aarav, Roll No: 1");
});

app.listen(3000, () => {
    console.log("Server started at http://localhost:3000");
});
