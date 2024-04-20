from flask import Flask, send_from_directory
from api.patientsAPI import patientsAPI
from api.chatAPI import chatAPI
from flask_cors import CORS

# from api import patientAPI


app = Flask(__name__)
CORS(app)


@app.route("/chat")
def chatbot():
    return send_from_directory("static", "chat.html")


@app.route("/translate")
def translator():
    return send_from_directory("static", "translator.html")


app.register_blueprint(patientsAPI)
app.register_blueprint(chatAPI)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


if __name__ == "__main__":

    app.run(debug=True)
