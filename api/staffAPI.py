from flask import Blueprint, jsonify, request
from extensions import coordinator
import json

# from app import socketio


staffAPI = Blueprint("staffAPI", __name__, url_prefix="/staff")


@staffAPI.route("/emergencies/<int:nurseID>")
def getAllEmergencies(nurseID: int):
    if coordinator.nurse_exists_by(nurseID):
        try:
            lijst = coordinator.get_emergencies_nurse(nurseID)
            return jsonify({"message": lijst}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 501
    else:
        return jsonify({f"error": "No nurse with id {nurseID}"}), 404


@staffAPI.route("/chatmessages/<int:nurseID>")
def getAllChatMessages(nurseID: int):
    if coordinator.nurse_exists_by(nurseID):
        try:
            lijst = coordinator.get_chatmessage_nurse(nurseID)
            return jsonify({"message": lijst}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 501
    else:
        return jsonify({f"error": "No nurse with id {nurseID}"}), 404
