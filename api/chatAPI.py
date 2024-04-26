from flask import Blueprint, jsonify, request
from model import MyChatBot
from extensions import patients_db, nurse
from logic.chatmessage import ChatMessage
import requests

chatbot = MyChatBot()
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
    if data is not None and data["query"] is not None and data["id"] is not None:
        query = data["query"]
        id = data["id"]
        try:
            # this logic will later reside in COORDINATOR class
            patient = patients_db.get_patient_by(id)
            chat = ChatMessage(
                data["query"],
                id,
            )
            nurse.notify(chatEl, id)
            antwoord = chatbot.final_result(query)
            return jsonify({"message": antwoord["result"]})
        except Exception as e:
            return jsonify({"error": str(e)}), 404
    else:
        return jsonify({"error": "query and or id not present"}), 400
