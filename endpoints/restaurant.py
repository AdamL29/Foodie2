from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check


# Restaurant Endpoint!
@app.get('/api/restaurant')
def get_restaurant():
    id = request.args.get('restaurantId')
    keys = ["name", "address", "city", "email", "phoneNum", "bio"]
    results = run_statement("CALL get_restaurant(?)", [id])
    response = []
    if (type(results) == list):
        for rests in results:
            response.append(dict(zip(keys, rests)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 500)

@app.post('/api/restaurant')
def add_restaurant():
    keys = ["name", "address", "city", "email", "phoneNum", "password", "bio"]
    name = request.json.get('name')
    address = request.json.get('address')
    city = request.json.get('city')
    email = request.json.get('email')
    phoneNum = request.json.get('phoneNum')
    password = request.json.get('password')
    bio = request.json.get('bio')
    results = run_statement("CALL create_restaurant (?,?,?,?,?,?,?)", [name, address, city, email, phoneNum, password, bio])
    response = []
    if (type(results) == list):
        for restaurant in results:
            response.append(dict(zip(keys, restaurant)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)

@app.patch('/api/restaurant')
def update_restaurant():
    keys = ["name", "address", "city", "email", "phoneNum", "password", "bio"]
    name = request.json.get('name')
    address = request.json.get('address')
    city = request.json.get('city')
    email = request.json.get('email')
    phoneNum = request.json.get('phoneNum')
    password = request.json.get('password')
    bio = request.json.get('bio')
    id = request.json.get('restaurantId')
    results = run_statement("CALL update_restaurant (?,?,?,?,?,?,?,?)", [name, address, city, email, phoneNum, password, bio, id])
    response = []
    if (type(results) == list):
        for restaurant in results:
            response.append(dict(zip(keys, restaurant)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500)
