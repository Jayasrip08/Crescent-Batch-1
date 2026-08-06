"""
Day 37 — Authentication Basics: user registration with password hashing.
Run schema.sql first, then: python app.py
Test /register in Postman, then check the users table — you should see a
long hash, never the raw password.
"""
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"status": "Day 37 Auth API is running"})


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    # Never store the raw password — hash it first.
    password_hash = generate_password_hash(data["password"])

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, password_hash)
        )
        conn.commit()
    except Exception:
        return jsonify({"error": "Username already exists"}), 400
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "User registered successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
