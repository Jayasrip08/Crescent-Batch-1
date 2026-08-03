const express = require("express");
const app = express();

const PORT = 8080;

// Middleware to parse JSON body
app.use(express.json()); // array to json this middleware is used to convert data types



// In-memory "database"
let students = [
    { id: 1, name: "Akhil", dept: "IT" },
    { id: 2, name: "Sara", dept: "CS" }   //session based. If the session gets deleted this will be removed
];


//Custom Middleware
function logger (req, res, next){
    
    console.log("Method:", req.method);
    console.log("URL:", req.url)
}

app.use(logger);

// GET all students
app.get("/students", (req, res) => {
    res.json(students);
});

// GET student by ID
app.get("/students/:id", (req, res) => {
    const student = students.find(s => s.id === parseInt(req.params.id));
    if (!student) return res.status(404).send("Student not found");
    res.json(student);
});

// POST new student
app.post("/students", (req, res) => {
    const newStudent = {
        id: students.length + 1,
        name: req.body.name,
        dept: req.body.dept
    };
    students.push(newStudent);
    res.status(201).json(newStudent);
});

// PUT update student
app.put("/students/:id", (req, res) => {
    const student = students.find(s => s.id === parseInt(req.params.id));
    if (!student) return res.status(404).send("Student not found");

    student.name = req.body.name || student.name;
    student.dept = req.body.dept || student.dept;

    res.json(student); //console.log(data)
});

// DELETE student
app.delete("/students/:id", (req, res) => {
    const index = students.findIndex(s => s.id === parseInt(req.params.id));
    if (index === -1) return res.status(404).send("Student not found");

    const deleted = students.splice(index, 1);
    res.json(deleted[0]);
});

app.listen(PORT, () => {
    console.log("The app is running>>>>>");
});
