from flask import Flask, send_from_directory

# from api import patientAPI


app = Flask(__name__)

# app.register_blueprint(patientAPI)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/chat")
def chatbot():
    return send_from_directory("static", "chat.html")


if __name__ == "__main__":

    app.run(debug=True)
