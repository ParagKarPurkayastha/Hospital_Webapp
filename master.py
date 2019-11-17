from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


application = Flask(__name__)
CORS(application)

# database connections
cluster = MongoClient("mongodb+srv://Purkayastha:Qwerty12%@hospitaldata-7shyu.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["hospital"]

currentLoginEmail = "none"
chatData = []


def chatSet():
    collection = db["liveChat"]
    collection.delete_many({})
    data = {
        "person": "intern",
        "text": "How you doin?"
    }
    collection.insert_one(data)


chatSet()


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
        "password": password
    }

    # print(data)
    collection.insert_one(data)
    # print(name)
    return "ok"


@application.route('/login', methods=['POST'])
def login():
    email = request.json["email"]
    password = request.json["pass"]
    print(email, password)
    collection = db["registerData"]
    result = collection.find({ "email": email })
    relPass = ""
    for i in result:
            relPass = i["password"]
    # print(data)
    if password == relPass:
        global currentLoginEmail
        currentLoginEmail = email
        # print(currentLoginEmail)
        return jsonify({"valid": "true"})
    else:
        return jsonify({"valid": "false"})


@application.route('/loginData', methods=['POST'])
def loginData():
    global currentLoginEmail
    collection = db["registerData"]
    result = collection.find({ "email": currentLoginEmail })
    data = []
    for i in result:
        data = {
            "name": i["name"],
            "diag": i["diag"],
        }

    return jsonify({"loginData": data})


@application.route('/DocLogin', methods=['POST'])
def docLogin():
    email = request.json["email"]
    password = request.json["pass"]
    print(email, password)
    collection = db["doctorsData"]
    result = collection.find({ "email": email })
    relPass = ""
    for i in result:
        relPass = i["password"];

    # print(data)
    if password == relPass:
        return jsonify({"valid": "true"})
    else:
        return jsonify({"valid": "false"})


@application.route('/getAllData', methods=['GET'])
def getAllData():
    return jsonify({"chatData": chatData})


@application.route('/chatDataSend', methods=['POST'])
def chatDataSend():
    collection = db["liveChat"]
    text = request.json["chatData"]

    data = {
        "person": "user",
        "text": text
    }

    print(text)
    collection.insert_one(data)
    return "ok"


@application.route('/chatDataGet', methods=['GET'])
def chatDataGet():
    collection = db["liveChat"]
    results = collection.find({})
    global chatData

    allChatData = []
    for result in results :
        chat = {
            "person": result["person"],
            "text": result["text"]
        }
        allChatData.append(chat)

    print(chatData, allChatData)
    data = []
    for i in range(len(allChatData) - len(chatData)):
        temp = {
            "person": allChatData[len(chatData) + i]["person"],
            "text": allChatData[len(chatData) + i]["text"]
        }
        data.append(temp)

    chatData = allChatData
    # print(data)
    return jsonify({"chatData": data})


if __name__ == '__main__':
    application.run(debug=True)
    #application.run(host='0.0.0.0')

