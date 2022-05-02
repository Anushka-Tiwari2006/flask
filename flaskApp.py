from flask import Flask,jsonify,request

app = Flask(__name__)
contacts = []

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data."
        },400)

    contact = {
        "id":contacts [-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    contacts.append(contact)
    return jsonify({"status":"success","message":"Contact added successfully"})


if __name__ == "__main__":
    app.run(debug = True)

        







