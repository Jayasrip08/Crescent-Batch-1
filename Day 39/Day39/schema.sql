-- Day 39 — replace this with YOUR own individual project's schema.
-- This is just a shape to start from.

CREATE DATABASE IF NOT EXISTS your_project_db;
USE your_project_db;

CREATE TABLE IF NOT EXISTS predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    input_data VARCHAR(500),
    predicted_result VARCHAR(255),
    confidence DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
