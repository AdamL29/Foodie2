from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

# Orders Endpoint!
@app.get('/api/orders')
def get_orders():
    id = request.args.get('id')
    keys = ["createdAt", "ifConfirmed", "isCancelled", "isComplete", "restId", "clientId"]
    results = run_statement("CALL get_orders(?)", [id])
    if (type(results) == list):
        for orders in results:
            zipped = zip(keys, orders)
            orders = (dict(zipped))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)
