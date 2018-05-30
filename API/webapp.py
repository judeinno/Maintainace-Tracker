from flask import Flask, request,  jsonify
import os


app = Flask(__name__)

login_successful={
                'success':True,
                'message':"Login in Succesfully.",
                'token':123
                }
login_fail={
        'success':False,
        'message':"Login Failed."
        }
auth_fail={
        'success':False,
        'message':"You are not authorised to access this page."
        }
request_fail={
        'success':False,
        'message':"Not a valid Request ID."
        }
create_request_fail={
        'success':False,
        'message':"All fields required."
        }
create_request_successful={
        'success':True,
        'message':"Your request was submitted successfully.",
        'token':123
        }

requests = [{'id': 1,'Field': u'Environment','SubField': u'Grass','RequestType': u'Maintenance','RequestStatus':u'Resolved'},{'id': 1,'Field': u'Electricity','SubField': u'bulb','RequestType': u'replace','RequestStatus':u'Not yet approved'}]


#Making an API Endpoint (GET)
@app.route('/')
def api_documentation():
    return "Maintenance-Tracker"

@app.route('/api/v1/login', methods=['POST'])
def api_login():
    data = request.args
    email = data.get("email")
    password = data.get("password")
    
    if email == "jud@gmail.com":
        if password == "12345":
            return jsonify(login_successful)
        else:
            return jsonify(login_fail)
    else:
        return jsonify(login_fail)


@app.route('/api/v1/requests')
def api_get_requests():
    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '12qwe1':
        return jsonify(requests)
    else:
        return jsonify(auth_fail)

@app.route('/api/v1/users/requests/<requestId>', methods=['GET'])
def api_get_logged_in_user_requests(requestId):
    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '12qwe1':
        if int(requestId) < len(requests) and int(requestId) >= 0:   
            return jsonify(requests[int(requestId)])
        else:
            return jsonify(request_fail)
    else:
        return jsonify(auth_fail)

@app.route('/api/v1/users/requests', methods=['POST'])
def api_create_request():
    data = request.args
    requestField=data.get("Field")
    requestSubField = data.get("SubField")
    requestRequestType=data.get("RequestType")
    requestDetails=data.get("Details")
    requestRequestStatus=data.get("Requeststatus")

    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '12qwe1':
        if requestField!= None and requestSubField!= None and requestRequestType!= None and requestDetails!= None and requestStatus!= None:
            return jsonify(create_request_successful)
        else:
            return jsonify(create_request_fail)
    else:
        return jsonify(auth_fail)

@app.route('/api/v1/users/requests/<requestId>', methods=['PUT'])
def api_modify_request(requestId):
    data = request.args
    requestField=data.get("Field")
    requestSubField = data.get("SubField")
    requestRequestType=data.get("RequestType")
    requestDetails=data.get("Details")
    requestRequestStatus=data.get("Requeststatus")

    try:
        token = request.headers["Authorization"]
    except:
        return jsonify(auth_fail)

    if token == '12qwe1':
        if int(requestId) < len(requests) and int(requestId) >= 0:   
            if requestField!= None and requestSubField!= None and requestRequestType!= None and requestDetails!= None and requestStatus!= None:
                return jsonify(create_request_successful)
            else:
                return jsonify(create_request_fail)
        else:
            return jsonify(request_fail)
    return jsonify(auth_fail)

if __name__ == '__main__':
    app.run(debug=True)