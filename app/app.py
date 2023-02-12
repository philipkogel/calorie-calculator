"""Main app file"""
from flask import Flask
from models import Temperature
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'

    return app


flask_app = create_app()
temp = Temperature(country='poland', city='warsaw')
temp.get()