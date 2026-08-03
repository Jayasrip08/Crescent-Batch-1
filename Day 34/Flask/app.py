from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
students = [
    {"id": 1, "name": "Akhil", "dept": "IT"},
    {"id": 2, "name": "Sara", "dept": "CS"}
]

# GET all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)  #json format

# GET student by ID
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return "Student not found", 404
    return jsonify(student)

# POST new student
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    new_student = {
        "id": len(students) + 1, # adding a data cell 
        "name": data.get("name"),
        "dept": data.get("dept")
    }
    students.append(new_student)
    return jsonify(new_student), 201

# PUT update student
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return "Student not found", 404

    data = request.get_json()
    student["name"] = data.get("name", student["name"])
    student["dept"] = data.get("dept", student["dept"])
    return jsonify(student)

# DELETE student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    global students
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return "Student not found", 404

    students = [s for s in students if s["id"] != id]
    return jsonify(student)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
