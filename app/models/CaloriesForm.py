from wtforms import StringField, FormField, IntegerField, FloatField, Form, SubmitField
from wtforms.validators import DataRequired

class CaloriesForm(Form):
    height = FloatField(
        label='Height',
        validators=[DataRequired()],
        description='Enter height in cm'
    )
    weight = FloatField(
        label='Weight',
        validators=[DataRequired()],
        description='Enter weight in kg'
    )
    age = IntegerField(label='Age', validators=[DataRequired()], description="20")
    city = StringField(label='City', validators=[DataRequired()], description="Warsaw")
    country = StringField(label='Country', validators=[DataRequired()], description="Poland")

    submit = SubmitField(label='Submit')
