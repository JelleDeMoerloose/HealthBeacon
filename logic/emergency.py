class Emergency:
    def __init__(self, patientID, nurseID, button, timestamp):
        self.patientID = patientID 
        self.nurseID = nurseID
        self.button = button #bool for wether patient clicked on emergency button or not 
        self.timestamp = timestamp
        
    def set_question(self, question):
        self.question = question #only if emergency got triggered through a chatbot question