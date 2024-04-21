
from flask import Flask, send_from_directory, request, jsonify
from api.patientsAPI import patientsAPI
from api.chatAPI import chatAPI
from api.nurseAPI import nurseAPI
from flask_cors import CORS



app = Flask(__name__)
CORS(app)



@app.route("/chat")
def chatbot():
    return send_from_directory("static", "chat.html")

@app.route("/nurse")
def nurse():
    return send_from_directory("static", "nurse.html")

app.register_blueprint(patientsAPI)
app.register_blueprint(chatAPI)
app.register_blueprint(nurseAPI)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")




@app.route("/notify", methods=["POST"])
def handle_new_question():
    data = request.json
    print("data ", data)
    if data["question"] is not None:
        print('New question received:', data["question"])
      
        socketio.emit('new_question', data["question"])
    return jsonify({"message": "succesfully notified a nurse"})


if __name__ == "__main__":


    app.run(debug=True)
