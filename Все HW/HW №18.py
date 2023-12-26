import json
from typing import Set


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


class Cities:
    def __init__(self, city_data):
        self.city_data = city_data
        self.city_names_set = self.create_cities_names_set()

    def create_cities_names_set(self):
        cities_names_set = set()
        for city_info in self.city_data:
            if city_info['name'][:-1] != 'ёьъы'
                cities_names_set.add(city_info['name'])
        return cities_names_set


class CityGame:
    def __init__(self, cities: Cities):
        self.cities_object = cities
        self.cities_set: Set[str] = self.cities_object.city_names_set
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
        if self.human_city not in self.cities_set:
            print(f'Города {self.human_city} отсутствует в списке городов')
            return False
        if self.ai_city:
            if not self.check_game_rules(self.ai_city, self.human_city):
                print(f'Ваш город {self.human_city} начинается не с той буквы')
                return False
        self.cities_set.remove(self.human_city)
        return True

    def ai_turn(self):
        for city_by_ai in self.cities_set:
            if self.check_game_rules(self.human_city, city_by_ai):
                print(f'Компьютер назвал город: {city_by_ai}')
                self.ai_city = city_by_ai
                return True
            else:
                print('Поздравляют! Вы победили')
                return False


class GameManager:
    def __init__(self, json_file: JsonFile, cities: Cities, game: CityGame):
        self.json_file = json_file
        self.cities = cities
        self.game = game

    def __start_game(self):
        while True:
            if not self.game.human_turn():
                break
            if not self.game.ai_turn():
                break

    def __call__(self):
        self.__start_game()
        input('Игра завершена. Нажмите Enter для выхода. ')


if __name__ == "__main__"
