"""Main app file"""
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'

    return app


flask_app = create_app()
