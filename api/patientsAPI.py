from flask import Blueprint, jsonify




patientsAPI = Blueprint('patientsAPI', __name__, url_prefix='/patients')

@patientsAPI.route('/all')
def get_resource():
    return jsonify({'data': 'This is your resource'})