from flask import Flask, send_from_directory, request, jsonify
from flask_socketio import SocketIO, emit
from api.patientsAPI import patientsAPI
from api.staffAPI import staffAPI
from api.dashboardAPI import dashboardAPI
from flask_cors import CORS

from extensions import app
from extensions import socketio



CORS(app)

# Dictionary to store nurse IDs and corresponding sockets
nurse_sockets = {}


@app.route("/home")
def home():
    return send_from_directory("static", "homescreen.html")


@app.route("/chat")
def chatbot():
    return send_from_directory("static", "chat.html")


@app.route("/companion")
def companion():
    return send_from_directory("static", "companion.html")


@app.route("/schedule")
def schedule():
    return send_from_directory("static", "schedule.html")


@app.route("/nurse")
def nurse():
    return send_from_directory("static", "nurse.html")


@app.route("/translator")
def translator():
    return send_from_directory("static", "translator.html")

@app.route("/dashboard")
def dashboard():
    return send_from_directory("static", "dashboard2.html")


@app.route("/websocket")
def websocket():
    return send_from_directory("static", "websocket.html")

app.register_blueprint(patientsAPI)
app.register_blueprint(staffAPI)
app.register_blueprint(dashboardAPI)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


"""
@app.route("/notify", methods=["POST"])
def handle_new_question():
    data = request.json
    print("data ", data)
    if data["question"] is not None:
        print("New question received:", data["question"])

        socketio.emit("new_question", data["question"])
    return jsonify({"message": "succesfully notified a nurse"})

"""
@socketio.on("connect", namespace="/websocket")  # Specify the namespace
def handle_connect():
    print(f"Nurse connected")


@socketio.on("disconnect", namespace="/websocket")  # Specify the namespace
def handle_disconnect():
    nurse_id = request.args.get("nurse_id")
    del nurse_sockets[nurse_id]
    print(f"Nurse {nurse_id} disconnected")





"""
if __name__ == "__main__":
    socketio.run(app, use_reloader=True, log_output=True)
    print("test")

"""
socketio.run(app, use_reloader=True, log_output=True)
print("test")