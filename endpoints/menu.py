from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

@app.post('/api/menu')
def create_item():
    keys = ['name', 'description', 'price']
    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')