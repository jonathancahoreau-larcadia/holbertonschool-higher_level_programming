#!/usr/bin/python3
"""Simple RESTful API example using Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """Endpoint for the home page."""
    return "Welcome to the Flask API!", 200


@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys())), 200


@app.route("/status", methods=["GET"])
def get_status():
    return "OK", 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is not None:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    user_name = data.get("username")
    if user_name is None:
        return jsonify({"error": "Username is required"}), 400

    if user_name in users:
        return jsonify({"error": "Username already exists"}), 409

    users[user_name] = data
    return jsonify({
                "message": "User added",
                "user": data
            }), 201


if __name__ == "__main__":
    app.run("", port=5000)
