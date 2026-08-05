from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# ----------------------------------
# Logger Middleware
# ----------------------------------

@app.before_request
def logger():
    print("-------------------------")
    print("Method :", request.method)
    print("URL    :", request.path)
    print("-------------------------")

# ----------------------------------
# MySQL Connection
# ----------------------------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",          # Password from installing MySQL
    database="college_db"
)

# ----------------------------------
# Home Route
# ----------------------------------

@app.route("/", methods=["GET"])
def home():
    return "Student REST API"

# ----------------------------------
# GET All Students
# ----------------------------------

@app.route("/students", methods=["GET"])
def get_all_students():
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM students"
    
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return jsonify(result), 200
    except mysql.connector.Error as err:
        return jsonify({"message": str(err)}), 500
    finally:
        cursor.close()

# ----------------------------------
# GET Student By ID
# ----------------------------------

@app.route("/students/<int:id>", methods=["GET"])
def get_student_by_id(id):
    cursor = db.cursor(dictionary=True)
    sql = "SELECT * FROM students WHERE id = %s"
    
    try:
        cursor.execute(sql, (id,))
        result = cursor.fetchall()
        
        if len(result) == 0:
            return jsonify({"message": "Student Not Found"}), 404
        
        return jsonify(result[0]), 200
    except mysql.connector.Error as err:
        return jsonify({"message": str(err)}), 500
    finally:
        cursor.close()

# ----------------------------------
# POST Student
# ----------------------------------

@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    department = data.get("department")
    
    cursor = db.cursor()
    sql = "INSERT INTO students (name, age, department) VALUES (%s, %s, %s)"
    
    try:
        cursor.execute(sql, (name, age, department))
        db.commit()
        return jsonify({
            "message": "Student Added",
            "id": cursor.lastrowid
        }), 201
    except mysql.connector.Error as err:
        db.rollback()
        return jsonify({"message": str(err)}), 500
    finally:
        cursor.close()

# ----------------------------------
# PUT Student
# ----------------------------------

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    department = data.get("department")
    
    cursor = db.cursor()
    sql = "UPDATE students SET name = %s, age = %s, department = %s WHERE id = %s"
    
    try:
        cursor.execute(sql, (name, age, department, id))
        db.commit()
        
        if cursor.rowcount == 0:
            return jsonify({"message": "Student Not Found"}), 404
        
        return jsonify({"message": "Student Updated"}), 200
    except mysql.connector.Error as err:
        db.rollback()
        return jsonify({"message": str(err)}), 500
    finally:
        cursor.close()

# ----------------------------------
# DELETE Student
# ----------------------------------

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    cursor = db.cursor()
    sql = "DELETE FROM students WHERE id = %s"
    
    try:
        cursor.execute(sql, (id,))
        db.commit()
        
        if cursor.rowcount == 0:
            return jsonify({"message": "Student Not Found"}), 404
        
        return jsonify({"message": "Student Deleted"}), 200
    except mysql.connector.Error as err:
        db.rollback()
        return jsonify({"message": str(err)}), 500
    finally:
        cursor.close()

# ----------------------------------
# Start Server
# ----------------------------------

if __name__ == "__main__":
    print("Connected to MySQL")
    app.run(port=3000, debug=True)