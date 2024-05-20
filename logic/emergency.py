from datetime import datetime
import json


class Emergency:
    def __init__(self, patientID, nurseID, button):
        self.patient_id = patientID
        self.nurse_id = nurseID
        self.button = (
            button  # bool for wether patient clicked on emergency button or not
        )
        self.timestamp = datetime.now()

    def __str__(self) -> str:
        return self.toJSON()

    def toJSON(self):
        # Create a dictionary of the object's attributes
        emergency_dict = {
            "patient_id": self.patient_id,
            "nurse_id": self.nurse_id,
            "button": self.button,
            "timestamp": self.timestamp.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),  # Convert datetime to ISO 8601 string
        }
        # Convert the dictionary to a JSON string
        return json.dumps(emergency_dict)
