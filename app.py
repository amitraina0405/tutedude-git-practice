from flask import Flask,render_template,request,jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET", "POST"])
def todo():
   message = None
   if request.method == "POST":
       item_name = request.form.get("itemName")
       item_description = request.form.get("itemDescription")
       message = f"Item '{item_name}' added with description: {item_description}"
   return render_template("todo.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)
