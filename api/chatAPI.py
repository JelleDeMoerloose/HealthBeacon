from flask import Blueprint, jsonify, request
from model import MyChatBot

chatbot = MyChatBot()
chatAPI = Blueprint("chatAPI", __name__, url_prefix="/chat")


@chatAPI.route("/", methods=["POST"])
def get_answer():
    if request.is_json:
        # Access the JSON data sent in the request body
        data = request.json
        if data:
            print("Received JSON data:", data["query"])
            antwoord = chatbot.final_result(data["query"])
            return jsonify({"message": antwoord["result"]})
        else:
            return jsonify({"error": "Request body must be in JSON format"}), 400
    else:
        return jsonify({"error": "Request body must be in JSON format"}), 400
