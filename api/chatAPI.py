from flask import Blueprint, jsonify, request
#from model import MyChatBot
from extensions import patients_db, nurse
import requests

#chatbot = MyChatBot()
chatAPI = Blueprint("chatAPI", __name__, url_prefix="/chat")


@chatAPI.route("/", methods=["POST"])
def get_answer():
    if request.is_json:
      
        data = request.json
        if data:
            print("Received JSON data:", data["query"])
            antwoord = chatbot.final_result(data["query"])
            return jsonify({"message": antwoord["result"]})
        else:
            return jsonify({"error": "Request body must be in JSON format"}), 400
    else:
        return jsonify({"error": "Request body must be in JSON format"}), 400


@chatAPI.route("/v2", methods=["POST"])
def get_answerv2():

    data = request.json

    print(data)

    if(data["query"] is not None and data["id"] is not None):

        query = data["query"]
        id = data["id"]

    
       

        patient = patients_db.get_patient_by_id(id)
        if patient is None:
            return jsonify({'error': 'Patient not found'}), 404
        else:

            chatEl = patient.add_chatElement(data["query"])
            post_data = {"question": query}
            print("post_data", post_data)
            #hier nog een select best suitable nurse
            nurse.notify(chatEl, id)
          
            #antwoord = chatbot.final_result(data["query"])
            #return jsonify({"message": antwoord["result"]})
            return jsonify({"message": "ok"})
    else:
        return jsonify({"error": "query and or id not present"}), 400
   
