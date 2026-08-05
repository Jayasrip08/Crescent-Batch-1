const express = require("express");
const mysql = require("mysql2");

const app = express();

app.use(express.json());

/* ----------------------------------
   Logger Middleware
----------------------------------- */

function logger(req, res, next) {

    console.log("-------------------------");
    console.log("Method :", req.method);
    console.log("URL    :", req.url);
    console.log("-------------------------");

    next();

}

app.use(logger);

/* ----------------------------------
   MySQL Connection
----------------------------------- */

const db = mysql.createConnection({

    host: "localhost",
    user: "root", //Remember the user
    password: "", // Password from installing mysql
    database: "college_db"

});

db.connect((err) => {

    if (err) {
        console.log(err);
        return;
    }

    console.log("Connected to MySQL");

});

/* ----------------------------------
   Home Route
----------------------------------- */

app.get("/", (req, res) => {

    res.send("Student REST API");

});

/* ----------------------------------
   GET All Students
----------------------------------- */

app.get("/students", (req, res) => {

    const sql = "SELECT * FROM students"; //get all the data

    db.query(sql, (err, result) => {

        if (err) {

            return res.status(500).json({
                message: err.message
            });

        }

        res.status(200).json(result);

    });

});

/* ----------------------------------
   GET Student By ID
----------------------------------- */

app.get("/students/:id", (req, res) => {

    const id = req.params.id;

    const sql = "SELECT * FROM students WHERE id=?";

    db.query(sql, [id], (err, result) => {

        if (err) {

            return res.status(500).json({
                message: err.message
            });

        }

        if (result.length == 0) {

            return res.status(404).json({
                message: "Student Not Found"
            });

        }

        res.json(result[0]);

    });

});

/* ----------------------------------
   POST Student
----------------------------------- */

app.post("/students", (req, res) => {

    const { name, age, department } = req.body;

    const sql =

        "INSERT INTO students(name,age,department) VALUES(?,?,?)";

    db.query(sql,

        [name, age, department],

        (err, result) => {

            if (err) {

                return res.status(500).json({
                    message: err.message
                });

            }

            res.status(201).json({

                message: "Student Added",

                id: result.insertId

            });

        });

});

/* ----------------------------------
   PUT Student
----------------------------------- */

app.put("/students/:id", (req, res) => {

    const id = req.params.id;

    const { name, age, department } = req.body;

    const sql =

        "UPDATE students SET name=?, age=?, department=? WHERE id=?";

    db.query(

        sql,

        [name, age, department, id],

        (err, result) => {

            if (err) {

                return res.status(500).json({
                    message: err.message
                });

            }

            if (result.affectedRows == 0) {

                return res.status(404).json({
                    message: "Student Not Found"
                });

            }

            res.json({
                message: "Student Updated"
            });

        });

});

/* ----------------------------------
   DELETE Student
----------------------------------- */

app.delete("/students/:id", (req, res) => {

    const id = req.params.id;

    const sql =

        "DELETE FROM students WHERE id=?";

    db.query(

        sql,

        [id],

        (err, result) => {

            if (err) {

                return res.status(500).json({
                    message: err.message
                });

            }

            if (result.affectedRows == 0) {

                return res.status(404).json({
                    message: "Student Not Found"
                });

            }

            res.json({
                message: "Student Deleted"
            });

        });

});

/* ----------------------------------
   Start Server
----------------------------------- */

const PORT = 3000;

app.listen(PORT, () => {

    console.log(`Server running on port ${PORT}`);

});