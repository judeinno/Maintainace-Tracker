from flask import Flask, request,  jsonify
import os

app = Flask(__name__)

@app.route('/API/user/requests', methods=['GET'])
def fetch():
    pass

@app.route('/API/user/requests', methods=['POST'])
def create():
    pass