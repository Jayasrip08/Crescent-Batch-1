"""
Day 36 — CRUD with a Database.
Run schema.sql first, then: python app.py
Test every route below in Postman.
"""
from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"status": "Day 36 CRUD API is running"})


# ---------- CREATE ----------
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
    cursor.close()
    conn.close()
    return jsonify({"id": new_id, "message": "Item created"}), 201


# ---------- READ (all) ----------
@app.route("/items", methods=["GET"])
def get_items():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)


# ---------- READ (one) ----------
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item)


# ---------- UPDATE ----------
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
    cursor.close()
    conn.close()
    if not updated:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Item updated"})


# ---------- DELETE ----------
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    deleted = cursor.rowcount
    cursor.close()
    conn.close()
    if not deleted:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True)
