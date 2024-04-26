class Patient:
    def __init__(
        self,
        patient_id: int,
        contagious_disease: bool,
        surgery_type: str,
        treatment_type: str,
        days_in_hospital: int,
    ):
        self.id = patient_id
        self.contagious_disease = contagious_disease
        self.surgery_type = surgery_type
        self.treatment_type = treatment_type
        self.days_in_hospital = days_in_hospital
        self.chat = []

    def __str__(self):

        return f"Patient ID: {self.id}, Contagious Disease: {self.contagious_disease}, Surgery Type: {self.surgery_type}, Treatment Type: {self.treatment_type}, Days in Hospital: {self.days_in_hospital}"

    def serialize(self):
        keys = [
            "id",
            "contagious_disease",
            "surgery_type",
            "treatment_type",
            "days_in_hospital",
        ]
        serialized_patient = {key: getattr(self, key) for key in keys}
        return serialized_patient
