from app import app
from flask import Flask, make_response, jsonify, request
from dbhelpers import run_statement
from check import check
from dbcreds import production_mode
from flask_cors import CORS
from uuid import uuid4
# uuid4 generates a random token

# Client Login Endpoint!
@app.post('/api/client-login')
def client_login():
    # required = ['email', 'password']
    # check_info = check(request.json, required)
    # if check_info != None:
    #     return check_info
    token = uuid4().hex
    # creates random UUID
    email = request.json.get("email")
    password = request.json.get("password")
    results = run_statement("CALL client_login (?,?,?)", [email, password, token])
    if (type(results) == list):
        if results[0][0] == 1:
            return make_response(jsonify(results), 200)
        elif results[0][0] == 0:
            return make_response(jsonify("Sign in Failed"), 500)
    else:
        return make_response(jsonify(results), 500)