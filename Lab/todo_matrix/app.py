from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson import ObjectId


# --------------------------------------------------
# 1. CREATE FLASK APPLICATION
# --------------------------------------------------

app = Flask(__name__)


# --------------------------------------------------
# 2. CONNECT TO MONGODB
# --------------------------------------------------

client = MongoClient("mongodb://localhost:27017/")

db = client["todo_matrix"]

tasks_collection = db["tasks"]


# --------------------------------------------------
# 3. HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# 4. GET ALL TASKS
# --------------------------------------------------

@app.route("/api/tasks", methods=["GET"])
def get_tasks():

    tasks = tasks_collection.find()

    task_list = []

    for task in tasks:

        task_data = {
            "id": str(task["_id"]),
            "title": task["title"],
            "importance": task["importance"],
            "urgency": task["urgency"]
        }

        task_list.append(task_data)

    return jsonify(task_list)


# --------------------------------------------------
# 5. ADD A NEW TASK
# --------------------------------------------------

@app.route("/api/tasks", methods=["POST"])
def add_task():

    data = request.json

    title = data.get("title")
    importance = data.get("importance")
    urgency = data.get("urgency")

    # Check that the task title exists
    if not title:
        return jsonify({
            "error": "Task title is required"
        }), 400

    # Importance must be 0 or 1
    if importance not in [0, 1]:
        return jsonify({
            "error": "Importance must be 0 or 1"
        }), 400

    # Urgency must be 0 or 1
    if urgency not in [0, 1]:
        return jsonify({
            "error": "Urgency must be 0 or 1"
        }), 400

    # Create the task
    new_task = {
        "title": title,
        "importance": importance,
        "urgency": urgency
    }

    # Insert into MongoDB
    result = tasks_collection.insert_one(new_task)

    return jsonify({
        "message": "Task added successfully",
        "id": str(result.inserted_id)
    }), 201


# --------------------------------------------------
# 6. DELETE A TASK
# --------------------------------------------------

@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):

    try:
        object_id = ObjectId(task_id)

    except:
        return jsonify({
            "error": "Invalid task ID"
        }), 400

    result = tasks_collection.delete_one({
        "_id": object_id
    })

    if result.deleted_count == 0:
        return jsonify({
            "error": "Task not found"
        }), 404

    return jsonify({
        "message": "Task deleted successfully"
    })


# --------------------------------------------------
# 7. RUN FLASK SERVER
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)