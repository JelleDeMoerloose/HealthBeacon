from flask import Blueprint, jsonify, request


import json
from extensions import coordinator

# import sys
# sys.path.append("..")


patientsAPI = Blueprint("patientsAPI", __name__, url_prefix="/patients")


@patientsAPI.route("/chat", methods=["POST"])
def get_answer():

    data = request.json
    if data is not None and data["query"] is not None and data["id"] is not None:
        query = data["query"]
        id = data["id"]
        try:
            # this logic will later reside in COORDINATOR class
            antwoord = coordinator.question_asked(query, id)
            return jsonify({"message": antwoord})
        except Exception as e:
            return jsonify({"error": str(e)}), 404
    else:
        return jsonify({"error": "query and or id not present"}), 400


@patientsAPI.route("/translate", methods=["GET"])
def get_all_languages():
    return jsonify(coordinator.all_known_languages()), 200


@patientsAPI.route("/translate", methods=["POST"])
def translate():
    json_data = request.json
    if json_data:
        lang = json_data.get("lang")  # Using get method to avoid KeyError
        text = json_data.get("text")
        # Do something with the JSON data
        if lang and text:
            return jsonify({"translation": coordinator.translate_to(text, lang)}), 200
        else:
            return jsonify({"error": "JSON has wrong arguments"}), 400

    else:
        return jsonify({"error": "No JSON data received"}), 400


@patientsAPI.route("/id/<int:id>")
def patient_exists_with(id):

    if coordinator.patient_exists_by(id):
        return jsonify({"exists": True}), 200
    else:
        return jsonify({"exists": False}), 200
