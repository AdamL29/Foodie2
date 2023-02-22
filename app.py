from flask import Flask, make_response, jsonify, request
from dbhelpers import run_statement
from dbcreds import production_mode
from flask_cors import CORS
import client.client as client

app = Flask(__name__)
CORS(app)

@app.get('/api/client')
def get_clients():
    return client.get_clients()

@app.post('/api/client')
def add_client():
    return client.add_client()



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