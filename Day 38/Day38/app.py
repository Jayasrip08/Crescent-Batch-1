"""
Day 38 — Sessions & Login.
Builds on Day 37: adds /login, /logout, and a login_required-protected route.
Run Day37/schema.sql first if you haven't, then: python app.py

Test flow in Postman, in this order:
1. POST /register   (skip if you already have a user from Day 37)
2. POST /login       -> Postman stores the session cookie automatically
3. GET  /profile     -> should succeed while logged in
4. POST /logout      -> clears the session
5. GET  /profile     -> should now return 401
"""
from functools import wraps
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_connection

app = Flask(__name__)
app.secret_key = "change-this-to-a-real-secret-key"  # TODO: use a real secret in production


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Please log in first"}), 401
        return f(*args, **kwargs)
    return decorated


@app.route("/")
def home():
    return jsonify({"status": "Day 38 Sessions API is running"})


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    password_hash = generate_password_hash(data["password"])
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (data["username"], password_hash)
        )
        conn.commit()
    except Exception:
        return jsonify({"error": "Username already exists"}), 400
    finally:
        cursor.close()
        conn.close()
    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (data["username"],))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user or not check_password_hash(user["password_hash"], data["password"]):
        return jsonify({"error": "Invalid username or password"}), 401

    # Session persists across requests via a cookie Postman/the browser stores.
    session["user_id"] = user["id"]
    session["username"] = user["username"]
    return jsonify({"message": f"Welcome back, {user['username']}!"})


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"})


@app.route("/profile", methods=["GET"])
@login_required
def profile():
    return jsonify({"username": session["username"]})


if __name__ == "__main__":
    app.run(debug=True)
