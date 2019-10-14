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
    # name = "boom Bom"
    name = name[1:]
    print(name)
    collection = db["doctorsData"]
    result = collection.find({ "name": name })
    data = []
    for i in result:
        data = { "data": i["data"] }
    print(data)
    return jsonify({"doctor_names": "ok"})


if __name__ == '__main__':
    application.run(debug=True)
    #application.run(host='0.0.0.0')

