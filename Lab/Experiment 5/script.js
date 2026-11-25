// Demonstrating JavaScript Arrays

let students = ["Harshil", "Rahul", "Amit", "Priya"];

// Display all students
console.log("Student List:", students);

// Access an element
console.log("First Student:", students[0]);

// Add a new student
students.push("Neha");
console.log("After Adding:", students);

// Remove the last student
students.pop();
console.log("After Removing:", students);

// Display array length
console.log("Total Students:", students.length);

// Demonstrating JavaScript Objects

let student = {
    id: 101,
    name: "Harshil",
    course: "B.Tech CSE",
    semester: 5
};

// Display the complete object
console.log("Student Details:", student);

// Access object properties
console.log("Student Name:", student.name);
console.log("Student Course:", student.course);

// Modify an object property
student.semester = 6;
console.log("Updated Semester:", student.semester);

// Add a new property
student.city = "Dehradun";
console.log("Updated Student Details:", student);

// Demonstrating JavaScript Functions

// Function to display a message
function greet() {
    console.log("Welcome to JavaScript Functions!");
}

// Function with parameters
function addNumbers(a, b) {
    return a + b;
}

// Function to calculate square
function calculateSquare(number) {
    return number * number;
}

// Calling functions
greet();

let sum = addNumbers(10, 20);
console.log("Sum of Numbers:", sum);

let square = calculateSquare(5);
console.log("Square of Number:", square);