import json

from logic.patient import Patient
from logic.nurse import Nurse
from logic.chatmessage import ChatMessage
from abc import ABC, abstractmethod
from logic.emergency import Emergency


class IContext(ABC):
    @abstractmethod
    def add_patient(self, patient: Patient):
        pass

    @abstractmethod
    def remove_patient(self, patient_id: int):
        pass

    @abstractmethod
    def get_patient_by(self, id: int) -> Patient | None:
        pass

    @abstractmethod
    def get_all_patients(self) -> list[Patient]:
        pass

    @abstractmethod
    def get_nurse_by(self, id: int) -> Nurse | None:
        pass

    @abstractmethod
    def get_all_nurses(self) -> list[Nurse]:
        pass

    @abstractmethod
    def add_chat_message(self, chatmessage: ChatMessage):
        pass

    @abstractmethod
    def add_emergency(self, emergency: Emergency):
        pass

    @abstractmethod
    def get_emergency_timestamps(self) -> list:
        pass

    @abstractmethod
    def get_chat_history_patient(self, patient_id: int) -> list[ChatMessage]:
        pass

    @abstractmethod
    def get_chat_history_nurse(self, nurse_id: int) -> list[ChatMessage]:
        pass

    @abstractmethod
    def get_emergency_history_nurse(self, nurse_id) -> list[Emergency]:
        pass

    @abstractmethod
    def get_emergency_history_patient(self, patient_id) -> list[Emergency]:
        pass


class HardcodedContext(IContext):
    DATA_PATH = "data/patients.json"

    def __init__(self, socket):
        self.socket = socket
        self.patient_dict: dict[int, Patient] = {}
        self.nurses_dict: dict[int, Nurse] = {}
        self.messages: list[ChatMessage] = []
        self.emergencies: list[Emergency] = []
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

    def get_patient_by(self, patient_id: int) -> Patient | None:

        return self.patient_dict.get(patient_id)

    def get_all_patients(self):
        return list(self.patient_dict.values())

    def get_nurse_by(self, id: int) -> Nurse | None:
        return self.nurses_dict.get(id)

    def get_all_nurses(self) -> list[Nurse]:
        return list(self.nurses_dict.values())

    def add_chat_message(self, chatmessage: ChatMessage):
        self.socket.emit(
            "notification",
            {"message": chatmessage.toJSON(), "chatmessage": True},
        )
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

    def add_emergency(self, emergency: Emergency):
        if (
            emergency.button
        ):  # if not by button, its already sent to nurse with chatmessage
            self.socket.emit(
                "notification",
                {"message": emergency.toJSON(), "chatmessage": False},
            )
        self.emergencies.append(emergency)

    def get_emergency_history_nurse(self, nurse_id) -> list[Emergency]:
        filtered_messages = filter(
            lambda message: message.nurse_id == nurse_id, self.emergencies
        )
        return list(filtered_messages)

    def get_emergency_history_patient(self, patient_id) -> list[Emergency]:
        filtered_messages = filter(
            lambda message: message.patient_id == patient_id, self.emergencies
        )
        return list(filtered_messages)

    def get_emergency_timestamps(self) -> list:
        timestamps = []
        for emergency in self.emergencies:
            timestamps.append(emergency.timestamp)
        return timestamps
