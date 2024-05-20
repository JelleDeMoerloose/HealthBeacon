from flask import Blueprint, jsonify, request
from extensions import coordinator
import json
from datetime import datetime
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



@staffAPI.route("/emergencies/dashboard/all", methods=["GET"])
def emergencies_all():

    now = datetime.now()

    # Extract the hour component from the current time
    current_hour = now.hour
    hours_until_now = [str(hour) + ":00" for hour in range(current_hour + 1)]

    data = [30, 20, 25, 26, 21, 22, 23, 24, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]

    emergencies = coordinator.get_emergencies()

    today_emergencies = [emergency for emergency in emergencies if emergency.date() == datetime.today().date()]
    hourly_emergencies = [emergency.hour for emergency in today_emergencies]



    for em in hourly_emergencies:
        data[em] = data[em]+1







    # Return the list as JSON
    return jsonify({"label": hours_until_now, "data": data[:len(hours_until_now)], "extra": hourly_emergencies})
