from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check


# Restaurant Endpoint!
@app.get('/api/restaurant')
def get_restaurant():
    id = request.args.get('restaurantId')
    keys = ["name", "address", "city", "email", "phoneNum", "bio"]
    result = run_statement("CALL get_restaurant(?)", [id])
    if (type(result) == list):
        for clients in result:
            zipped = zip(keys, clients)
            clients = (dict(zipped))
            # response.append(dict(zip(keys, clients)))
        return make_response(jsonify(result), 200)
    else:
        return make_response(jsonify(result), 500)

@app.post('/api/restaurant')
def add_restaurant():
    keys = ["username", "firstName", "lastName", "email", "password"]
    userName = request.json.get('username')
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    email = request.json.get('email')
    password = request.json.get('password')
    results = run_statement("CALL create_restaurant (?,?,?,?,?)", [userName, firstName, lastName, email, password])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)

@app.patch('/api/restaurant')
def update_restaurant():
    keys = ["username", "firstName", "lastName", "email"]
    id = request.json.get('userId')
    userName = request.json.get('username')
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    email = request.json.get('email')
    password = request.json.get('password')
    results = run_statement("CALL update_restaurant (?,?,?,?,?,?)", [id, userName, firstName, lastName, email, password])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)
