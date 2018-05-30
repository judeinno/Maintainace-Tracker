from flask import Flask, request,  jsonify
import os

app = Flask(__name__)

@app.route('/API/user/requests', methods=['GET'])
def fetch():
    return jsonify({"message":"success"})

@app.route('/API/user/requests', methods=['POST'])
def create():
    pass