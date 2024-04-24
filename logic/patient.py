from logic.chatElement import ChatElement
class Patient:
    def __init__(self, patient_id, contagious_disease, surgery_type, treatment_type, days_in_hospital):
        self.id = patient_id
        self.contagious_disease = contagious_disease
        self.surgery_type = surgery_type
        self.treatment_type = treatment_type
        self.days_in_hospital = days_in_hospital
        self.chat = []

    def __str__(self):
        
        return f"Patient ID: {self.id}, Contagious Disease: {self.contagious_disease}, Surgery Type: {self.surgery_type}, Treatment Type: {self.treatment_type}, Days in Hospital: {self.days_in_hospital}"

    def serialize(self):
        keys = ['id', 'contagious_disease', 'surgery_type', 'treatment_type', 'days_in_hospital']
        serialized_patient = {key: getattr(self, key) for key in keys}
        return serialized_patient

    def add_chatElement(self, question: str):
        newChatEl = ChatElement(question)
        self.chat.append(newChatEl)
        return newChatEl

    def get_chat_history(self):
        return self.chat
    
    def get_latest_chat(self):
        return self.chat[-1]
