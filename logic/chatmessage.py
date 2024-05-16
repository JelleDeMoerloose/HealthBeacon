from datetime import datetime


class ChatMessage:
    def __init__(
        self,
        question: str,
        patient_id: int,
        nurse_id: int,
        category: int,
        timestamp=datetime.now(),
    ):
        self.question = question
        self.patient_id = patient_id
        self.nurse_id = nurse_id
        self.category = category
        self.timestamp = timestamp
        self.val = None  #

    def set_answer(self, answer):
        self.answer = answer

    def validate(self, choosen_category):
        self.val = choosen_category  # used to check if predictions were right

    def __str__(self):
        return f"Question: {self.question}\nPatient ID: {self.patient_id}\nNurse ID: {self.nurse_id}\nCategory: {self.category}\nTimestamp: {self.timestamp}\nValue: {self.val}"

    def serialize(self):
        keys = ["question", "answer", "category"]
        serialized_chatElement = {key: getattr(self, key) for key in keys}
        return serialized_chatElement
