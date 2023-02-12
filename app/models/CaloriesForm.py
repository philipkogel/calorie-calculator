from wtforms import StringField, FormField, IntegerField, FloatField, Form

class CaloriesForm(Form):
    weight = FloatField(label='Weight')
    height = FloatField(label='Height')
    age = IntegerField(label='Age')
    city = StringField(label='City')
    country = StringField(label='Country')
