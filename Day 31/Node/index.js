const express = require("express");
const app = express();
const path = require("path");
const PORT = 8080;


app.get('/', (req, res) => {
    res.send("Hello")
});

app.get('/about', (req, res) => {
    res.send("Student")
});
app.use(express.static(path.join(__dirname, "public")));

app.get('/contact', (req, res) => {
    res.sendFile(path.join(__dirname, "views", "index.html")) //__dirname = D:\Crescent\Day 31\Node
});

app.listen(PORT, () => {
    console.log("Server is running...")
})