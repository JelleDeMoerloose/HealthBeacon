from flask import Flask, send_from_directory, request, jsonify
from flask_socketio import SocketIO, emit
from api.patientsAPI import patientsAPI
from api.staffAPI import staffAPI
from flask_cors import CORS


app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)

# Dictionary to store nurse IDs and corresponding sockets
nurse_sockets = {}


@app.route("/chat")
def chatbot():
    return send_from_directory("static", "chat.html")


@app.route("/nurse")
def nurse():
    return send_from_directory("static", "nurse.html")


@app.route("/translate")
def translator():
    return send_from_directory("static", "translator.html")


app.register_blueprint(patientsAPI)
app.register_blueprint(staffAPI)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@socketio.on("connect", namespace="/websocket")  # Specify the namespace
def handle_connect():
    nurse_id = request.args.get("nurse_id")
    nurse_sockets[nurse_id] = request.sid
    print(f"Nurse {nurse_id} connected")


@socketio.on("disconnect", namespace="/websocket")  # Specify the namespace
def handle_disconnect():
    nurse_id = request.args.get("nurse_id")
    del nurse_sockets[nurse_id]
    print(f"Nurse {nurse_id} disconnected")


# Example event for sending notifications
def send_notification(nurse_id, message):
    if nurse_id in nurse_sockets:
        socketio.emit(
            "notification",
            {"message": message},
            room=nurse_sockets[nurse_id],
            namespace="/websocket",
        )  # Specify the namespace


if __name__ == "__main__":

    socketio.run(app, use_reloader=True, log_output=True)
