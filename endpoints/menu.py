from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

# Menu Endpoint!
@app.get('/api/menu')
def get_menu():
    id = request.args.get('restaurantId')
    keys = ["name", "description", "price", "imageUrl"]
    results = run_statement("CALL get_menu(?)", [id])
    response = []
    if (type(results) == list):
        for menu in results:
            response.append(dict(zip(keys, menu)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 500)

@app.post('/api/menu')
def create_item():
    required = ['token']
    check_info = check(request.json, required)
    if check_info != None:
        return check_info
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
    required = ['token']
    check_info = check(request.json, required)
    if check_info != None:
        return check_info
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
    required = ['token']
    check_info = check(request.json, required)
    if check_info != None:
        return "Deleted"
    id = request.json.get("menuId")
    results = run_statement("CALL delete_item`(?)", id)
    if(type(results) == list):
        return make_response(jsonify("Delete Successful"), 200)
    else:
        return make_response(jsonify(results), 500)