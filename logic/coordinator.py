from logic.context import IContext
from logic.nurse_select import INurseSelect
from logic.patient import Patient
from logic.nurse import Nurse
from logic.translator import ITranslator
from logic.chatmessage import ChatMessage
from model import IChatBot
import json


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

    def question_asked(self, query: str, id: int) -> str:

        patient: Patient | None = self.context.get_patient_by(id)
        if patient is None:
            raise NameError(f"Patient with id {id} does not exist")

        nurse: Nurse = self.nurse_selector.select_nurse(id)
        print(f"Nurse with id {nurse.id} choosen to handle request")
        antwoord = self.chatbot.final_result(query, patient)
        fake_json = antwoord["result"]
        python_dict = json.loads(fake_json)
        category = 0  # 0= no assistance needed, 1= help is needed , 2= emergency
        help_bool: bool = bool(python_dict["help"])
        emergency_bool: bool = bool(python_dict["emergency"])
        if emergency_bool:
            category = 2
        elif help_bool:
            category = 1
        chat: ChatMessage = ChatMessage(
            query, id, nurse.id, category
        )  # timestamp is default
        # implement notifications to nurses and dashboarding

        self.context.add_chat_message(chat)
        print(chat)
        return python_dict["simple_answer"]

    def all_known_languages(self) -> dict[str, str]:
        return self.translator.all_languages()

    def translate_to(self, message: str, lang_to_lang: str):
        return self.translator.translate(message, lang_to_lang)

    def patient_exists_by(self, id: int) -> bool:
        patient: Patient | None = self.context.get_patient_by(id)
        if patient:
            return True
        return False
