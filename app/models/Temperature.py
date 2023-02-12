""" Temperature model """
import  requests
from selectorlib import Extractor


class Temperature:
    """
    Represents a temperature value extracted from timeanddate.com/weather webpage.
    """
    __yml_path = 'temperature.yml'
    __url = 'https://www.timeanddate.com/weather/'
    __extractor = Extractor.from_yaml_file(__yml_path)
    def __init__(self, country, city) -> None:
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')

    def get(self) -> float:
        res = requests.get(f'{self.__url}{self.country}/{self.city}')
        data = self.__extractor.extract(res.text)
        if data['temp'] is None:
            return None
        return float(data['temp'].replace('\xa0°C', ''))
