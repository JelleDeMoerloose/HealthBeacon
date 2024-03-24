from flask import Flask, send_from_directory



from api.patientsAPI import patientsAPI



app = Flask(__name__)

app.register_blueprint(patientsAPI)


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')



if __name__ == '__main__':
    
    app.run(debug=True)