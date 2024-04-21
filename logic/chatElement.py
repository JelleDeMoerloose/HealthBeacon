class ChatElement:
    def __init__(self, question):
        self.question = question
        self.answer = None

    def set_answer(self, answer):
        self.answer = answer

    def __str__(self):
        if self.answer is not None:
            return f"Q: {self.question}\nA: {self.answer}"
        else:
            return f"Q: {self.question}\nA: No answer yet"

    def serialize(self):
        keys = ['question', 'answer']
        serialized_chatElement = {key: getattr(self, key) for key in keys}
        return serialized_chatElement