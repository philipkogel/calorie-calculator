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
    age = IntegerField(label='Age', validators=[DataRequired()])
    city = StringField(label='City', validators=[DataRequired()])
    country = StringField(label='Country', validators=[DataRequired()])

    submit = SubmitField(label='Submit')
