from flask import Flask

app = Flask(__name__)

from endpoints import client, restaurant, auth, menu, orders