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
    response = []
    if (type(results) == list):
        for orders in results:
            response.append(dict(zip(keys, orders)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 500)

@app.post('/api/orders')
def add_orders():
    keys = ["orderId", "items"]
    restId = request.json.get('restId')
    items = request.json.get('items')
    results = run_statement("CALL create_order (?,?)", [restId, items])
    response = []
    if (type(results) == list):
        for orders in results:
            response.append(dict(zip(keys, orders)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)

@app.patch('/api/orders')
def update_orders():
    keys = ["orderId", "items"]
    id = request.json.get('orderId')
    restId = request.json.get('restId')
    items = request.json.get('items')
    results = run_statement("CALL update_order (?,?)", [id, restId, items])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)