""" Calorie model """
from User import User

class Calorie(User):
    """
    Represents amount of calories for the user calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """
    def __init__(self, temperature, **kwargs):
        super().__init__(**kwargs)
        self.temperature = temperature


    def calculate(self):
        """Calculate calories from gathered data"""
        pass