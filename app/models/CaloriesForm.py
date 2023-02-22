from wtforms import StringField, FormField, IntegerField, FloatField, Form, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError


class CaloriesForm(Form):
    height = IntegerField(
        label='Height',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=250)
        ],
        description='Enter height in cm'
    )
    weight = IntegerField(
        label='Weight',
        validators=[DataRequired(), NumberRange(min=1, max=600)],
        description='Enter weight in kg'
    )
    age = IntegerField(
        label='Age',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=120)
        ],
        description="20"
    )
    city = StringField(label='City', validators=[DataRequired()], description="Warsaw")
    country = StringField(label='Country', validators=[DataRequired()], description="Poland")

    submit = SubmitField(label='Submit')

