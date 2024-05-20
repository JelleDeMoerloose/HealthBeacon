from flask import Blueprint, jsonify, request
import json
from datetime import datetime
import random
from extensions import coordinator


dashboardAPI = Blueprint("dashboardAPI", __name__, url_prefix="/dashboard")



@dashboardAPI.route("/emergencies/all", methods=["GET"])
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

    

