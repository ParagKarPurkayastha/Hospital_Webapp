from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


application = Flask(__name__)
CORS(application)

# database connections
cluster = MongoClient("mongodb+srv://Purkayastha:Qwerty12%@hospitaldata-7shyu.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["hospital"]

chatData = []


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

