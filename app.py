from flask import Flask, jsonify
import json
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://<username>:<password>@<cluster-url>/todo_db?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

# Database and collection
db = client["todo_db"]
todos_collection = db["todos"]



@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
   try:
       data = request.get_json()  # Expecting JSON input
       item_name = data.get("itemName")
       item_description = data.get("itemDescription")
       if not item_name:
           return jsonify({"error": "Item Name is required"}), 400
       todo = {
           "itemName": item_name,
           "itemDescription": item_description
       }
       todos_collection.insert_one(todo)
       return jsonify({"message": "To-Do item added successfully", "todo": todo}), 201
   except Exception as e:
       return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
