""" User model """


class User:
    """
    Represents the collected user information
    """
    def __init__(self, weight, height, age) -> None:
        self.weight = weight
        self.height = height
        self.age = age
