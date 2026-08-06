"""
Day 39 — Individual Backend Project: Kickoff skeleton.
Adapt this to YOUR assigned project domain (see your Capstone Project
Assignment for your dataset, tech stack, and prediction target).

Steps:
1. Fill in schema.sql with your own tables.
2. Fill in routes_plan.md with your own routes.
3. Replace the TODOs below with your actual endpoints.
4. Confirm this runs and "/" responds before you build further.
"""
from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"status": "My individual project API is running"})


# TODO: add your CRUD routes here, following the Day 36 pattern
#   e.g. POST /api/predict, GET /api/history, GET /api/history/<id>

# TODO: add your ML model's predict endpoint here, following your Phase 2 model
#   Load your saved .pkl model once at startup, then call model.predict()
#   inside the route and return the result as JSON.


if __name__ == "__main__":
    app.run(debug=True)
