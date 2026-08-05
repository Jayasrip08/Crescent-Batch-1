"""
Day 36 — Database connection helper.
Every route in app.py calls get_connection() to talk to MySQL.
"""
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",   # TODO: replace with your own MySQL password
        database="innolift_demo"
    )
