""" Temperature model """
import  requests

class Temperature:
    """
    Represents a temperature value extracted from timeanddate.com/weather webpage.
    """
    __URL__ = 'https://www.timeanddate.com/weather/'
    def __init__(self, country, city) -> None:
        self.country = country
        self.city = city

    def get(self):
        res = requests.get(f'{self.__URL__}{self.country}/{self.city}')
        print(res.text)
        return res
