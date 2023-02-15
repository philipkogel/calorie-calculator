""" App main page class """
from flask.views import  MethodView
from flask import render_template
from .CaloriesForm import CaloriesForm

class HomePage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('index.html', calories_form=calories_form)
