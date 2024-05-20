from datetime import datetime
import json


class Emergency:
    def __init__(self, patientID, nurseID, button, timestamp=datetime.now()):
        self.patientID = patientID
        self.nurseID = nurseID
        self.button = (
            button  # bool for wether patient clicked on emergency button or not
        )
        self.timestamp = timestamp

    def toJSON(self):
        # Create a dictionary of the object's attributes
        emergency_dict = {
            "patientID": self.patientID,
            "nurseID": self.nurseID,
            "button": self.button,
            "timestamp": self.timestamp.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),  # Convert datetime to ISO 8601 string
        }
        # Convert the dictionary to a JSON string
        return json.dumps(emergency_dict)
