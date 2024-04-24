import json

from logic.patient import Patient


class Patients_db:

    DATA_PATH  = 'data/patients.json'


    def __init__(self):
        self.patient_dict = {}


    def initializer(self):
    
        patients = []

        with open(self.DATA_PATH, 'r') as f:
            data = json.load(f)

        for item in data:
            patient = Patient(item['id'],
                            item['contagious_disease'],
                            item['surgery_type'],
                            item['treatment_type'],
                            item['days_in_hospital'])

            self.patient_dict[patient.id] = patient

   
    def add_patient(self, patient):
        
        self.patient_dict[patient.id] = patient

    def remove_patient(self, patient_id):
      
        if patient_id in self.patient_dict:
            del self.patient_dict[patient_id]

    def get_patient_by_id(self, patient_id):
      
        return self.patient_dict.get(patient_id)

    def get_patients(self):

        return list(self.patient_dict.values())
