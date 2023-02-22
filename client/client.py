from flask import Flask, make_response, jsonify, request
from dbhelpers import run_statement
from dbcreds import production_mode
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    result = run_statement("CALL create_client(?,?,?,?,?)", [userName, firstName, lastName, email, password])
    response = []
    if (type(result) == list):
        for client in result:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(result), 200)
    else:
        return make_response(jsonify(result), 500)



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