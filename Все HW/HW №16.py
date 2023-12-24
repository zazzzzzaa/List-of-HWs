import json, csv

from typing import Union


class CsvFileHandler:
    def __init__(self, as_dict: bool, filepath):
        self.opened_file = None
        self.as_dict = as_dict
        self.filepath = filepath

    def read_file(self):
        if not self.as_dict:
            with open(self.filepath, 'r') as zero_some_csv_file:
                some_csv_file = csv.reader(zero_some_csv_file)
        else:
            some_csv_file = dict()
            with open(self.filepath, 'r') as zero_some_csv_file:
                second_zero_some_csv_file = csv.reader(zero_some_csv_file)
                for row in second_zero_some_csv_file:
                    some_csv_file += dict(second_zero_some_csv_file)
        self.opened_file = some_csv_file

    def write_file(self):
        print(self.opened_file)

    def append_file(self, data: Union[str, dict]):
        with open(self.filepath, 'w', newline='') as zero_some_csv_file:
            some_csv_file = csv.writer(zero_some_csv_file)
            some_csv_file.writerow(data)


class JsonFileHandler:
    def __init__(self, as_dict: bool, filepath):
        self.opened_file = None
        self.as_dict = as_dict
        self.filepath = filepath

    def read_file(self):
        if not self.as_dict:
            with open(self.filepath, 'r') as some_json_file:
                some_json_file = json.load(some_json_file)
        else:
            zero_some_json_file = open(self.filepath)
            some_json_file = json.load(zero_some_json_file)
        self.checker_for_read = True
        self.opened_file = some_json_file

    def write_file(self):
        print(self.opened_file)

    def append_file(self, data: Union[str, dict]):
        if not self.as_dict:
            if type(data) == dict:
                raise TypeError('Данный тип данных не поддерживается')
            with open(self.filepath, 'w') as another_json_file:
                json.dump(data, another_json_file)
        else:
            with open(self.filepath, 'w') as another_json_file:
                json.dump(dict(data), another_json_file)


class TxtFileHandler:
    def __init__(self, as_dict: bool, filepath):
        self.opened_file = None
        self.as_dict = as_dict
        self.filepath = filepath

    def read_file(self):
        some_txt_file = open(self.filepath).readline()
        self.opened_file = some_txt_file

    def write_file(self):
        print(self.opened_file)

    def append_file(self, data: str):
        some_txt_file = open(self.filepath).write(data)
       