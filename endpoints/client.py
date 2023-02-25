from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

# Client Endpoint!
@app.get('/api/client')
def get_clients():
    username = request.args.get('userName')
    keys = ["username", "firstName", "lastName", "email", "createdAt"]
    results = run_statement("CALL get_client(?)", [username])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 500)


@app.post('/api/client')
def add_client():
    keys = ["username", "firstName", "lastName", "email", "password"]
    userName = request.json.get('username')
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    email = request.json.get('email')
    password = request.json.get('password')
    results = run_statement("CALL create_client (?,?,?,?,?)", [userName, firstName, lastName, email, password])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)

@app.patch('/api/client')
def update_client():
    keys = ["username", "firstName", "lastName", "email"]
    id = request.json.get('userId')
    userName = request.json.get('username')
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    email = request.json.get('email')
    password = request.json.get('password')
    results = run_statement("CALL update_client (?,?,?,?,?,?)", [id, userName, firstName, lastName, email, password])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)


@app.delete('/api/client')
def delete_client():
    required = ['email']
    check_info = check(request.json, required)
    if check_info != None:
        return "Deleted"
    results = run_statement("CALL delete_client(?)", required)
    if(type(results) == list):
        return make_response(jsonify("Delete Successful"), 200)
    else:
        return make_response(jsonify(results), 500)

