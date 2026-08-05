import { useEffect, useState } from "react";
import "./App.css";

const API = import.meta.env.VITE_API_URL;

function App() {
  const [students, setStudents] = useState([]);

  const [form, setForm] = useState({
    name: "",
    dept: ""
  });

  const [editingId, setEditingId] = useState(null);

  // ==========================
  // GET ALL STUDENTS
  // ==========================
  const fetchStudents = async () => {
    try {
      const response = await fetch(`${API}/students`);  // API = VITE_API_URL = http://localhost/8080
      const data = await response.json();
      setStudents(data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  // ==========================
  // HANDLE INPUT
  // ==========================
  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  // ==========================
  // ADD STUDENT
  // ==========================
  const addStudent = async () => {
    if (!form.name || !form.dept) return;

    const response = await fetch(`${API}/students`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(form)
    });

    const data = await response.json();
    console.log(data);

    setForm({
      name: "",
      dept: ""
    });

    fetchStudents();
  };

  // ==========================
  // DELETE
  // ==========================
  const deleteStudent = async (id) => {
    await fetch(`${API}/students/${id}`, {
      method: "DELETE"
    });

    fetchStudents();
  };

  // ==========================
  // LOAD DATA INTO FORM
  // ==========================
  const editStudent = (student) => {
    setEditingId(student.id);

    setForm({
      name: student.name,
      dept: student.dept
    });
  };

  // ==========================
  // UPDATE
  // ==========================
  const updateStudent = async () => {
    await fetch(`${API}/students/${editingId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(form)
    });

    setEditingId(null);

    setForm({
      name: "",
      dept: ""
    });

    fetchStudents();
  };

  return (
    <div className="container">

      <h1>Student Management</h1>

      <div className="form">

        <input
          type="text"
          name="name"
          placeholder="Student Name"
          value={form.name}
          onChange={handleChange}
        />

        <input
          type="text"
          name="dept"
          placeholder="Department"
          value={form.dept}
          onChange={handleChange}
        />

        {editingId ? (
          <button onClick={updateStudent}>
            Update Student
          </button>
        ) : (
          <button onClick={addStudent}>
            Add Student
          </button>
        )}

      </div>

      <hr />

      {students.length === 0 ? (
        <h3>No Students Found</h3>
      ) : (
        students.map((student) => (
          <div className="card" key={student.id}>

            <h3>{student.name}</h3>

            <p>{student.dept}</p>

            <div className="buttons">

              <button onClick={() => editStudent(student)}>
                Edit
              </button>

              <button
                className="delete"
                onClick={() => deleteStudent(student.id)}
              >
                Delete
              </button>

            </div>

          </div>
        ))
      )}

    </div>
  );
}

export default App;