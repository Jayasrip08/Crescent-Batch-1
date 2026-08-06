"""
Day 38 — Database connection helper (same as Day 36/37).
"""
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",   # TODO: replace with your own MySQL password
        database="innolift_demo"
    )
