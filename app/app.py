"""Main app file"""
from flask import Flask
from models import HomePage
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.add_url_rule('/', view_func=HomePage.as_view('home-page'))

    return app


flask_app = create_app()
