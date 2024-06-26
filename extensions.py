from logic.context import IContext, HardcodedContext
from logic.nurse_select import INurseSelect, HardcodedNurseSelect
from model import IChatBot, ChatBotV1
from logic.coordinator import Coordinator
from logic.translator import ITranslator, TranslatorV1
from flask_socketio import SocketIO
from flask import Flask


app = Flask(__name__)
socketio = SocketIO(app)
# all objects and dependency injections
database: IContext = HardcodedContext(socketio)
nurse_selector: INurseSelect = HardcodedNurseSelect(database)
chatbot: IChatBot = ChatBotV1()
translator: ITranslator = TranslatorV1()
coordinator: Coordinator = Coordinator(database, chatbot, nurse_selector, translator)
