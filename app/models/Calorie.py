""" Calorie model """
from .User import User

class Calorie(User):
    """
    Represents amount of calories for the user calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """
    def __init__(self, temperature, **kwargs) -> None:
        super().__init__(**kwargs)
        self.temperature = temperature


    def calculate(self) -> float:
        """Calculate calories from gathered data"""
        return float(10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * self.temperature)