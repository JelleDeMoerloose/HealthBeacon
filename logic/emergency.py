from datetime import datetime


class Emergency:
    def __init__(self, patientID, nurseID, button, timestamp=datetime.now()):
        self.patientID = patientID
        self.nurseID = nurseID
        self.button = (
            button  # bool for wether patient clicked on emergency button or not
        )
        self.timestamp = timestamp
