from datetime import datetime


class ChatMessage:
    def __init__(
        self, question: str, patient_id: int, nurse_id: int, timestamp=datetime.now()
    ):
        self.question = question
        self.patient_id = patient_id
        self.nurse_id = nurse_id
        self.timestamp = timestamp

    def set_answer(self, answer):
        self.answer = answer

    def __str__(self):
        if self.answer is not None:
            return f"Q: {self.question}\nA: {self.answer}"
        else:
            return f"Q: {self.question}\nA: No answer yet"

    def serialize(self):
        keys = ["question", "answer"]
        serialized_chatElement = {key: getattr(self, key) for key in keys}
        return serialized_chatElement
