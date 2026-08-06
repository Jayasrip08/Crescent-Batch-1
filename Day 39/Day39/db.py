"""
Day 39 — Database connection helper. Update host/user/password/database
to match your own individual project's database name.
"""
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",   # TODO: replace with your own MySQL password
        database="your_project_db"  # TODO: replace with your own database name
    )
