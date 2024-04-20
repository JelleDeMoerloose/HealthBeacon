from flask import Blueprint, jsonify, request
from translator import ITranslator, TranslatorV1

import json

# import sys
# sys.path.append("..")


patientsAPI = Blueprint("patientsAPI", __name__, url_prefix="/patients")
translator: ITranslator = TranslatorV1()


@patientsAPI.route("/all")
def read_json_file():
    # Path to your JSON file
    json_file_path = "data/patients.json"

    try:
        # Open the JSON file and load its contents into a Python data structure
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        # Return the data as a JSON response
        return jsonify(data)

    except FileNotFoundError:
        return jsonify({"error": "JSON file not found"})


@patientsAPI.route("/id/<int:id>")
def get_patient_by_id(id):
    # Path to your JSON file
    json_file_path = "data/patients.json"

    try:
        # Open the JSON file and load its contents into a Python data structure
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        # Search for the patient with the specified ID
        patient = next((patient for patient in data if patient["id"] == id), None)

        if patient:
            return jsonify(patient)
        else:
            return jsonify({"error": "Patient not found"})

    except FileNotFoundError:
        return jsonify({"error": "JSON file not found"})


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
