from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


application = Flask(__name__)
CORS(application)

# database connections
cluster = MongoClient("mongodb+srv://Purkayastha:Qwerty12%@hospitaldata-7shyu.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["hospital"]

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route('/doctorNames', methods=['GET'])
def doctorNames():
    collection = db["doctorNames"]
    results = collection.find({})
    names = []
    for result in results :
        name = {"name": result["name"]}
        names.append(name)
    return jsonify({"doctor_names": names})


@application.route('/selectDoctor', methods=['POST'])
def selectDoctor():
    collection = db["selectedDoctor"]
    name = request.json["name"]
    data = {
        "name": name
    }
    collection.delete_many({})
    collection.insert_one(data)
    # print(name)
    return "ok"


@application.route('/getData', methods=['GET'])
def doctorsData():
    collection = db["selectedDoctor"]
    result = collection.find({})
    for i in result:
        name = i["name"]

    name = name[1:]
    print(name)
    collection = db["doctorsData"]
    result = collection.find({ "name": name })
    data = []
    for i in result:
        data = {
            "name": i["name"],
            "specialization": i["specialization"],
            "designation": i["designation"],
            "qualifications1": i["qualifications1"],
            "qualifications2": i["qualifications2"],
            "medical_experience1": i["medical_experience1"],
            "medical_experience2": i["medical_experience2"],
            "administrative_experience1": i["administrative_experience1"],
            "administrative_experience2": i["administrative_experience2"]
        }
    print(data)
    return jsonify({"doctorData": data})


@application.route('/register', methods=['POST'])
def register():
    collection = db["registerData"]
    name = request.json["name"]
    email = request.json["email"]
    cont = request.json["cont"]
    add = request.json["add"]
    diag = request.json["diag"]
    password = request.json["pass"]

    data = {
        "name": name,
        "email": email,
        "cont": cont,
        "add": add,
        "diag": diag,
        "pass": password
    }

    # print(data)
    collection.insert_one(data)
    # print(name)
    return "ok"


@application.route('/login', methods=['POST'])
def login():
    email = request.json["email"]
    password = request.json["pass"]

    collection = db["doctorsData"]
    result = collection.find({ "email": email })
    data = []
    for i in result:
        data = {
            "pass": i["pass"]
        }
    print(data)
    return jsonify({"pass": data})


if __name__ == '__main__':
    application.run(debug=True)
    #application.run(host='0.0.0.0')
