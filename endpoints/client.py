from flask import Flask, make_response, jsonify, request
from dbhelpers import run_statement
from check import check
from dbcreds import production_mode
from flask_cors import CORS
from uuid import uuid4
# uuid4 generates a random token

app = Flask(__name__)
CORS(app)

# Client Endpoint!
@app.get('/api/client')
def get_clients():
    id = request.args.get('clientId')
    keys = ["username", "firstName", "lastName", "email", "createdAt"]
    result = run_statement("CALL get_client(?)", [id])
    if (type(result) == list):
        for clients in result:
            zipped = zip(keys, clients)
            clients = (dict(zipped))
            # response.append(dict(zip(keys, clients)))
        return make_response(jsonify(result), 200)
    else:
        return make_response(jsonify(result), 500)

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

# Client post is creating a token.
# Creates user and logs in user, in 2 procedure calls in 1 python
# Procedure can be used with another procedure.
# Call procedures within procedures.

if (production_mode == True):
    print("Running server in production mode")
    import bjoern #type:ignore
    bjoern.run(app, "0.0.0.0", 5000)
else:
    print("Running in testing mode")
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)