from flask import Blueprint, jsonify, request
from translator import ITranslator, TranslatorV1

import json
from extensions import patients_db

# import sys
# sys.path.append("..")


patientsAPI = Blueprint("patientsAPI", __name__, url_prefix="/patients")
translator: ITranslator = TranslatorV1()


@patientsAPI.route("/all")
def read_json_file():
    patients = patients_db.get_patients()
    return jsonify([e.serialize() for e in patients])


@patientsAPI.route("/id/<int:id>")
def get_patient_by_id(id):
    patient = patients_db.get_patient_by_id(id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    else:
        return jsonify(patient.serialize()), 200


@patientsAPI.route("/translate", methods=["GET"])
def get_all_languages():
    return jsonify(translator.all_languages()), 200


@patientsAPI.route("/translate", methods=["POST"])
def translate():
    json_data = request.json
    if json_data:
        lang = json_data.get("lang")  # Using get method to avoid KeyError
        text = json_data.get("text")
        # Do something with the JSON data
        if lang and text:
            return jsonify({"translation": translator.translate(text, lang)}), 200
        else:
            return jsonify({"error": "JSON has wrong arguments"}), 400

    else:
        return jsonify({"error": "No JSON data received"}), 400

    

@patientsAPI.route('/chat/id/<int:id>/all')
def get_chathistory_by_patientid(id):
    patient = patients_db.get_patient_by_id(id)
    chat = patient.get_chat_history()

    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    else:
        return jsonify([e.serialize() for e in chat])

   
@patientsAPI.route('/chat/id/<int:id>/latest')
def get_chat_by_patientid(id):
    patient = patients_db.get_patient_by_id(id)
    

    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    else:
        chat = patient.get_latest_chat()
        return jsonify(chat.serialize())

