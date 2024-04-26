import json

from logic.patient import Patient
from logic.nurse import Nurse
from logic.chatmessage import ChatMessage
from abc import ABC, abstractmethod


class IContext(ABC):
    @abstractmethod
    def add_patient(self, patient: Patient):
        pass

    @abstractmethod
    def remove_patient(self, patient_id: int):
        pass

    @abstractmethod
    def get_patient_by(self, id: int) -> Patient:
        pass

    @abstractmethod
    def get_all_patients(self) -> list[Patient]:
        pass

    @abstractmethod
    def get_nurse_by(self, id: int) -> Nurse:
        pass

    @abstractmethod
    def get_all_nurses(self) -> list[Nurse]:
        pass

    @abstractmethod
    def add_chat_message(self, chatmessage: ChatMessage):
        pass

    @abstractmethod
    def get_chat_history_patient(self, patient_id: int) -> list[ChatMessage]:
        pass

    @abstractmethod
    def get_chat_history_nurse(self, nurse_id: int) -> list[ChatMessage]:
        pass


class HardcodedContext(IContext):
    DATA_PATH = "data/patients.json"

    def __init__(self):
        self.patient_dict: dict[int, Patient] = {}
        self.nurses_dict: dict[int, Nurse] = {}
        self.messages: list[ChatMessage] = []
        with open(self.DATA_PATH, "r") as f:
            data = json.load(f)

        # making ten hardcoded nurses
        for i in range(10):
            self.nurses_dict[i] = Nurse(i)

        for item in data:
            patient = Patient(
                item["id"],
                item["contagious_disease"],
                item["surgery_type"],
                item["treatment_type"],
                item["days_in_hospital"],
            )
            self.patient_dict[patient.id] = patient

    def add_patient(self, patient: Patient):
        self.patient_dict[patient.id] = patient

    def remove_patient(self, patient_id: int):
        if patient_id in self.patient_dict:
            del self.patient_dict[patient_id]

    def get_patient_by(self, patient_id: int) -> Patient:
        if patient_id in self.patient_dict:
            # error messages is not valid --> we already checked if NONE
            return self.patient_dict.get(patient_id)
        else:
            raise NameError(f"Patient with id {patient_id} not found!")

    def get_all_patients(self):
        return list(self.patient_dict.values())

    def get_nurse_by(self, id: int) -> Nurse:
        if id in self.nurses_dict:
            # error messages is not valid --> we already checked if NONE
            return self.nurses_dict.get(id)
        else:
            raise NameError(f"NursePatient with id {id} not found!")

    def get_all_nurses(self) -> list[Nurse]:
        return list(self.nurses_dict.values())

    def add_chat_message(self, chatmessage: ChatMessage):
        self.messages.append(chatmessage)

    def get_chat_history_patient(self, patient_id: int) -> list[ChatMessage]:
        # normally a join-query
        filtered_messages = filter(
            lambda message: message.patient_id == patient_id, self.messages
        )
        return list(filtered_messages)

    def get_chat_history_nurse(self, nurse_id: int) -> list[ChatMessage]:
        # normally a join-query
        filtered_messages = filter(
            lambda message: message.nurse_id == nurse_id, self.messages
        )
        return list(filtered_messages)
