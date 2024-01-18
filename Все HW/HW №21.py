from dataclasses import dataclass
from marshmallow import Schema, fields, post_load, INCLUDE, validate
import requests


def get_weather(city_name: str) -> dict:
    api_key = "1a69c964dd45d870d237c70ee71167c6"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()


@dataclass
class CurrentWeather:
    city_name: str
    weather_icon: str
    desc: str
    temp: float
    feels_like: float
    wind_speed: float

    def __str__(self):
        return f"Погода в городе {self.city_name}:\n" \
               f"Температура: {self.temp}°C\n" \
               f"Ощущается как: {self.feels_like}°C\n" \
               f"Скорость ветра: {self.wind_speed} м/с\n" \
               f"Погодные условия: {self.desc}"


class SchemaForCurrentWeather(Schema):
    city_name = fields.Str(data_key='name')
    weather_icon = fields.Str(data_key='weather.0.icon')
    desc = fields.Str(data_key='weather.0.description')
    temp = fields.Float(data_key='main.temp', validate=validate.Range(min=-10, max=70))
    feels_like = fields.Float(data_key='main.feels_like')
    wind_speed = fields.Float(data_key='wind.speed')

    @post_load
    def make_current_weather(self, data, **kwargs):
        return CurrentWeather(
            city_name=data['city_name'],
            weather_icon=data['weather'][0]['icon'],
            desc=data['weather'][0]['description'],
            temp=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            wind_speed=data['wind']['speed']
        )

    class Meta:
        unknown = INCLUDE


def main():
    user_city = input("Введите название города: ")
    weather_data = get_weather(user_city)
    schema = SchemaForCurrentWeather()
    current_weather = schema.load(weather_data)
    print(current_weather)


if __name__ == "__main__":
    main()
