""" App main page class """
from flask.views import  MethodView
from flask import render_template, request
from .CaloriesForm import CaloriesForm
from .Calorie import Calorie
from .Temperature import Temperature


class HomePage(MethodView):

    def get(self):
        calories_form = CaloriesForm()

        return render_template('index.html', calories_form=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)
        temperature = Temperature(country=calories_form.country.data, city=calories_form.city.data).get()
        calorie = Calorie(
            temperature=temperature,
            weight=calories_form.weight.data,
            height=calories_form.height.data,
            age=calories_form.age.data,
        ).calculate()

        return render_template('index.html', calories_form=calories_form, results={ 'temperature': temperature, 'calories': calorie })