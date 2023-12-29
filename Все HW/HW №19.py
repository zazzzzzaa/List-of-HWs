import json
from typing import List
from dataclasses import dataclass


class JsonFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        with open(self.file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def write_data(self, data):
        with open(self.file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False

    def __eq__(self, other):
        if isinstance(other, City):
            return self.name == other.name
        return False


class Cities:
    def __init__(self, city_data):
        self.city_data = city_data
        self.city_names_set = self.create_cities_names_list()

    def create_cities_names_list(self):
        cities_names_list = []
        for city_info in self.city_data:
            if city_info['name'][:-1] != 'ёьъы':
                cities_names_list.append(
                    City(
                        name=city_info['name'],
                        population=city_info['population'],
                        subject=city_info['subject'],
                        district=city_info['district'],
                        latitude=float(city_info['coords']['lat']),
                        longitude=float(city_info['coords']['lon'])
                    )
                )
        return cities_names_list


class CityGame:
    def __init__(self, cities: Cities):
        self.cities_object = cities
        self.cities_list: List[City] = self.cities_object.city_names_set
        self.human_city = ''
        self.ai_city = ''

    @staticmethod
    def check_game_rules(last_city: str, new_city: str) -> bool:
        if last_city[-1].lower() == new_city[0].lower():
            return True
        else:
            return False

    def human_turn(self):
        self.human_city = input('Введите ваш город: ').capitalize()
        if self.human_city == 'Стоп':
            print('Вы проиграли')
            return False
        for city in self.cities_list:
            if city.name == self.human_city:
                if city.is_used:
                    print(f'Город {self.human_city} уже был использован. Вы проиграли')
                    return False
                else:
                    self.human_city = city
                    break
        else:
            print(f'Города {self.human_city} нет в списке. Вы проиграли')
            return False
        if self.ai_city:
            if not self.check_game_rules(self.ai_city.name, self.human_city.name):
                print(f'Ваш город {self.human_city.name} начинается не с той буквы')
                return False
        self.human_city.is_used = True
        return True

    def ai_turn(self):
        for city in self.cities_list:
            if self.check_game_rules(self.human_city.name, city.name):
                if city.is_used:
                    continue
                print(f'Компьютер назвал город: {city.name}')
                self.ai_city = city
                city.is_used = True
                return True
        else:
            print('Поздравляют! Вы победили')
            return False


class GameManager:
    def __init__(self, json_file: JsonFile, cities: Cities, game: CityGame):
        self.json_file = json_file
        self.cities = cities
        self.game = game

    def start_game(self):
        while True:
            if not self.game.human_turn():
                break
            if not self.game.ai_turn():
                break

    def __call__(self):
        self.start_game()
        input('Игра завершена. Нажмите Enter для выхода. ')


if __name__ == "__main__":
    json_file = JsonFile("cities.json")
    cities = Cities(json_file.read_data())
    game = CityGame(cities)
    game_manager = GameManager(json_file, cities, game)
    game_manager()
