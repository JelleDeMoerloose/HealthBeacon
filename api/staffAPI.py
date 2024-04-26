from flask import Blueprint, jsonify, request

# from app import socketio


staffAPI = Blueprint("staffAPI", __name__, url_prefix="/staff")
