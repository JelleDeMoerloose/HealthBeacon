from datetime import datetime
import json


class ChatMessage:
    def __init__(
        self,
        question: str,
        patient_id: int,
        nurse_id: int,
        category: int = 0,
        answered: bool = False,
        timestamp=datetime.now(),
    ):
        self.question = question
        self.patient_id = patient_id
        self.nurse_id = nurse_id
        self.category = category
        self.timestamp = timestamp
        self.answered = answered
        self.val = None

    def set_answer(self, answer):
        self.answered = True
        self.answer = answer

    def validate(self, choosen_category):
        self.val = choosen_category  # used to check if predictions were right

    def __str__(self):
        return self.toJSON()

    def toJSON(self):
        obj = {
            "question": self.question,
            "patient_id": self.patient_id,
            "nurse_id": self.nurse_id,
            "category": self.category,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "answered": self.answered,
            "value": self.val,
        }
        return json.dumps(obj)
