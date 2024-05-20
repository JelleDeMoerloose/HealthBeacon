from logic.context import IContext
from logic.nurse_select import INurseSelect
from logic.patient import Patient
from logic.nurse import Nurse
from logic.translator import ITranslator
from logic.chatmessage import ChatMessage
from logic.emergency import Emergency
from model import IChatBot
import json
from datetime import datetime


class Coordinator:
    # inject dependencies in constructor
    def __init__(
        self,
        context: IContext,
        chatbot: IChatBot,
        nurse_select: INurseSelect,
        translator: ITranslator,
    ):
        self.context = context
        self.chatbot = chatbot
        self.nurse_selector = nurse_select
        self.translator = translator

        self.emergency_timestamps = []

    def question_asked(self, query: str, id: int) -> str:

        patient: Patient | None = self.context.get_patient_by(id)
        if patient is None:
            raise NameError(f"Patient with id {id} does not exist")

        nurse: Nurse = self.nurse_selector.select_nurse(id)
        print(f"Nurse with id {nurse.id} choosen to handle request")
        chat: ChatMessage = ChatMessage(query, id, nurse.id)  # timestamp is default

        # TODO: send to nurse and dashboard

        ###

        antwoord = self.chatbot.final_result(query, patient)
        fake_json = antwoord["result"]
        python_dict = json.loads(fake_json)
        category = 0  # 0= no assistance needed, 1= help is needed , 2= emergency
        help_bool: bool = bool(python_dict["help"])
        emergency_bool: bool = bool(python_dict["emergency"])
        if emergency_bool:
            emergency: Emergency = Emergency(
                id, self.nurse_selector.select_nurse(id), False
            )
            self.context.add_emergency(emergency)
            category = 2
        elif help_bool:
            category = 1

        chat.category = category
        # TODO: Send to nurse again with category

        ###
        chat.set_answer(python_dict["answer"])
        self.context.add_chat_message(chat)

        return python_dict["answer"]

    def all_known_languages(self) -> dict[str, str]:
        return self.translator.all_languages()

    def translate_to(self, message: str, lang_to_lang: str):
        return self.translator.translate(message, lang_to_lang)

    def patient_exists_by(self, id: int) -> bool:
        patient: Patient | None = self.context.get_patient_by(id)
        if patient:
            return True
        return False

    def nurse_exists_by(self, id: int) -> bool:
        nurse: Nurse | None = self.context.get_nurse_by(id)
        if nurse:
            return True
        return False

    def add_emergency(self, id: int):

        emergency: Emergency = Emergency(
            id, self.nurse_selector.select_nurse(id).id, False
        )
        self.context.add_emergency(emergency)

    def get_emergencies_nurse(self, id):
        emergencies = self.context.get_emergency_history_nurse(id)
        emergencies_str = [str(emergency) for emergency in emergencies]
        return emergencies_str

    def get_emergencies(self):

        return self.context.get_emergency_timestamps()
