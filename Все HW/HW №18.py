import json


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
