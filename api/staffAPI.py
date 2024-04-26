from flask import Blueprint, jsonify, request

from extensions import patients_db, nurse
import requests



nurseAPI = Blueprint('nurseAPI', __name__, url_prefix='/nurse')

@nurseAPI.route('/notifications/latest')
def get_notification():
    if(nurse.get_status is True):
        chat = nurse.get_latest()
        return jsonify({"question": chat[0].question, "patientId": chat[1] })
    else:
        return jsonify({"message": "no new notification"})

@nurseAPI.route('/notifications/all')
def get_notifications():
    # Collect all notifications from nurse instances
    
        all_notifications = nurse.get_all_notifications()

        return jsonify(all_notifications)
