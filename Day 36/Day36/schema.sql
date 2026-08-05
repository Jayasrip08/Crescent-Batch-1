-- Day 36 — run this in MySQL Workbench / CLI before starting app.py

CREATE DATABASE IF NOT EXISTS innolift_demo;
USE innolift_demo;

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10,2)
);
