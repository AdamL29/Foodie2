from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

# Menu Endpoint!
@app.post('/api/menu')
def create_item():
    keys = ['name', 'description', 'price', 'imageUrl', 'restId']
    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')
    imageUrl = request.json.get('imageUrl')
    restId = request.json.get("restId")
    results = run_statement("CALL create_item (?,?,?,?,?)", [name, description, price, imageUrl, restId])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 500)
    
@app.patch('/api/menu')
def edit_item():
    keys = ['id', 'name', 'description', 'price', 'imageUrl', 'restId']
    id = request.json.get('id')
    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')
    imageUrl = request.json.get('imageUrl')
    restId = request.json.get("restId")
    results = run_statement("CALL edit_item (?,?,?,?,?,?)", [id, name, description, price, imageUrl, restId])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)
    
@app.delete('/api/menu')
def delete_item():
    required = ['id']
    check_info = check(request.json, required)
    if check_info != None:
        return "Deleted"
    results = run_statement("CALL delete_client(?)", required)
    if(type(results) == list):
        return make_response(jsonify("Delete Successful"), 200)
    else:
        return make_response(jsonify(results), 500)