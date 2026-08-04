# Days 36–40 — Backend Deep Dive: CRUD, Auth & Your Individual Project

**Phase 04 · Backend Development · Full Stack AI Developer Program · Innolift Ventures**

This block is where Flask stops being "just an API demo" and becomes a real backend: a database behind it, real users with real passwords, real login sessions — and then each student builds their own individual backend project on top of it.

---

## Day 36 — CRUD with a Database (MySQL)

**Objective:** Build Create / Read / Update / Delete endpoints backed by a real MySQL table, not an in-memory Python list.

### 1. Setup

```bash
pip install flask mysql-connector-python
```

Create the database and table first (run this in MySQL Workbench / CLI):

```sql
CREATE DATABASE innolift_demo;
USE innolift_demo;

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10,2)
);
```

### 2. `db.py` — a reusable connection helper

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="innolift_demo"
    )
```

### 3. `app.py` — the four CRUD endpoints

```python
from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

# CREATE
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, description, price) VALUES (%s, %s, %s)",
        (data["name"], data.get("description"), data["price"])
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close(); conn.close()
    return jsonify({"id": new_id, "message": "Item created"}), 201

# READ (all)
@app.route("/items", methods=["GET"])
def get_items():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close(); conn.close()
    return jsonify(items)

# READ (one)
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    cursor.close(); conn.close()
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item)

# UPDATE
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET name=%s, description=%s, price=%s WHERE id=%s",
        (data["name"], data.get("description"), data["price"], item_id)
    )
    conn.commit()
    updated = cursor.rowcount
    cursor.close(); conn.close()
    if not updated:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Item updated"})

# DELETE
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    deleted = cursor.rowcount
    cursor.close(); conn.close()
    if not deleted:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)
```

### 4. Test it with Postman

| Method | URL | Body |
|---|---|---|
| POST | `http://localhost:5000/items` | `{"name":"Pen","description":"Blue ink","price":10.50}` |
| GET | `http://localhost:5000/items` | — |
| GET | `http://localhost:5000/items/1` | — |
| PUT | `http://localhost:5000/items/1` | `{"name":"Pen","description":"Black ink","price":12.00}` |
| DELETE | `http://localhost:5000/items/1` | — |

### 📝 Task for Day 36
Build the `items` CRUD API above (or adapt the table to your own domain — e.g. `books`, `products`, `tickets`). All 4 operations must work and be verified in Postman with screenshots of each request/response.

---

## Day 37 — Authentication Basics

**Objective:** Register real users safely — meaning their passwords are **never** stored as plain text.

### 1. Why password hashing matters
If your database is ever leaked, plaintext passwords expose every user instantly. Hashing turns `"mypassword123"` into something like `"pbkdf2:sha256:600000$..."` — one-way, so even you can't reverse it back to the original.

```bash
pip install werkzeug
```

### 2. `users` table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
```

### 3. Registration endpoint

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from db import get_connection

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
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
        cursor.close(); conn.close()

    return jsonify({"message": "User registered successfully"}), 201
```

Test in Postman: `POST /register` with `{"username": "afsin", "password": "mySecret123"}`. Then check the `users` table — you should see a long hash string, never the raw password.

### 📝 Task for Day 37
Build the `/register` endpoint above. Register at least 3 test users. Confirm in MySQL that only hashes are stored — take a screenshot of the `users` table showing hashed passwords.

---

## Day 38 — Sessions & Login

**Objective:** Let a registered user log in, stay logged in across requests, and log out — the flow behind every "Sign In" button you've ever used.

### 1. Login endpoint (session-based)

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash
from db import get_connection

app = Flask(__name__)
app.secret_key = "change-this-to-a-real-secret-key"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (data["username"],))
    user = cursor.fetchone()
    cursor.close(); conn.close()

    if not user or not check_password_hash(user["password_hash"], data["password"]):
        return jsonify({"error": "Invalid username or password"}), 401

    session["user_id"] = user["id"]
    session["username"] = user["username"]
    return jsonify({"message": f"Welcome back, {user['username']}!"})

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"})
```

### 2. Protecting routes — `login_required`

```python
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Please log in first"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/profile", methods=["GET"])
@login_required
def profile():
    return jsonify({"username": session["username"]})
```

### 3. Test the full flow in Postman
1. `POST /login` with valid credentials → note the session cookie Postman stores automatically.
2. `GET /profile` → should succeed while logged in.
3. `POST /logout` → clears the session.
4. `GET /profile` again → should now return `401 Please log in first`.

### 📝 Task for Day 38
Add `/login`, `/logout`, and one `@login_required`-protected route to your Day 37 app. Screenshot all 4 steps above in Postman, in order, proving the session actually blocks access after logout.

---

## Day 39 — Individual Backend Project: Kickoff

**Objective:** Start your own backend — the one tied to *your* assigned project domain and dataset (see your Capstone Project Assignment).

Today is planning + scaffolding, not finishing. Budget your time: **~40% planning, ~60% building.**

### Step 1 — Plan your API routes
Fill this table out for your own project before writing code:

| Method | Route | What it does |
|---|---|---|
| POST | `/api/...` | e.g. submit a new prediction request |
| GET | `/api/...` | e.g. fetch prediction history |
| GET | `/api/.../<id>` | e.g. fetch one record |
| PUT | `/api/...` | e.g. update a record |
| DELETE | `/api/...` | e.g. delete a record |

### Step 2 — Plan your database schema
Sketch every table and column before touching SQL:

```sql
-- Example shape — adapt fields to your actual project
CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    input_data VARCHAR(500),
    predicted_result VARCHAR(255),
    confidence DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 3 — Scaffold your Flask app
Start from this skeleton and adapt it to your domain:

```python
from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "API is running"})

# TODO: add your CRUD routes here, following your Day 36 pattern
# TODO: add your ML model's predict endpoint here, following your Phase 2 model

if __name__ == "__main__":
    app.run(debug=True)
```

### 📝 Task for Day 39
Submit: (1) your filled-in routes table, (2) your database schema SQL, and (3) a running skeleton Flask app with at least the `/` health-check route working. This is the plan you'll execute on Day 40.

---

## Day 40 — Individual Backend Project: Submit

**Objective:** Finish every endpoint you planned on Day 39, test everything, and push a clean, working backend to GitHub.

### Checklist before you submit

- [ ] Every route from your Day 39 plan is implemented and working
- [ ] Every endpoint tested in Postman — screenshot each request + response
- [ ] Passwords (if your project has auth) are hashed, never plaintext
- [ ] Database actually persists data — restart the server and confirm data is still there
- [ ] `.gitignore` excludes secrets (DB passwords, `venv/`, `__pycache__/`)
- [ ] Code pushed to GitHub with a clear `README.md` explaining how to run it
- [ ] Commit history shows real incremental progress, not one giant commit

### Suggested `README.md` for your project repo

```markdown
# [Your Project Name]

## What it does
[1-2 sentence description]

## Tech stack
Flask, MySQL, [your ML library]

## Setup
1. pip install -r requirements.txt
2. Create the database using schema.sql
3. python app.py

## API Endpoints
| Method | Route | Description |
|---|---|---|
| ... | ... | ... |
```

### 📝 Task for Day 40
Push your completed backend to GitHub. Submit the repo link + full Postman test screenshots for every endpoint in your Daily Task Submission Report.

---

## ✅ Submission (Days 36–40)
Fill out your Daily Task Submission Report for each day as usual, and submit via InnoTrack. For Days 39–40 specifically, your GitHub repo link is mandatory proof of work.

## 🔜 Next Up
**Day 41 — Full Stack Integration begins.** You'll connect this exact backend to a real React/HTML frontend — the pieces start becoming one live app.
