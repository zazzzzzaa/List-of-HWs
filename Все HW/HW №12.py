import json

from typing import Set, Any, Union

with open('../cities.json', 'r', encoding='utf-8') as file:
    cities_names = set(json.load(file))

turn = 0  # Это счётчик хода


def main(turn: int, cities: Set[str]) -> Any:
    """
    Основная функция
    :param turn: счётчик хода
    :param checker: счётчик для нахождения слова на нужную букву
    :param cities: все города
    :return:
    """
    while cities:
        city = city_hum()
        if not city_hum_checker(city, cities):
            return False
        if turn == 0:
            cities = city_hum_del_for_turn_1(cities, city)
        Ai_city = ''
        AI_city = city_AI(cities, city)
        if AI_city:
            cities = city_AI_checker(AI_city, cities)
        else:
            hum_win()
            return True


def city_hum() -> str:
    """
    Здесь человек вводит город и он записывается с большой буквы
    :return: возвращает город, выбранный человек после обработки
    """
    city = input("Введите название города РФ, оканчивающийся НЕ на ь/ъ/ы/ё, или остановите игру: ")
    city = city.title()
    return city


def city_hum_checker(city: str, cities: Set[str]) -> Union[str, bool]:
    """
    Проверяет на остановку игры, находится ли слово в сете слов
    :param city: город, названный игроком
    :param cities: Сет городов
    :return: возврат либо проигрышв, либо города игрока
    """
    if city in cities:
        return city
    elif city == 'Стоп' or city == 'стоп':
        print('Вы проиграли компьютеру :(')
        return False
    else:
        print("Такого города не существует или он уже был или он не удовлетворяет условию, вы проиграли")
        return False


def city_hum_del_for_turn_1(cities: Set[str], city: str) -> Set[str]:
    """
    удаляет слово игрока на первом ходу
    :param cities: сет городов
    :param city: город игрока
    :return: возвращаем сет городов после удаления города игрока
    """
    cities.discard(city)
    return cities


def city_AI(cities: Set[str], city: str) -> Any:
    """
    Здесь выводим город ИИ
    :param cities: сет городов
    :param city: город игрока
    :return: возвращаем город ИИ и счётчик
    """
    for name in cities:
        if name[0:1] == city[-1::].title():
            AI_city = name
            return AI_city


def city_AI_checker(AI_city: str, cities: Set[str]) -> Set[str]:
    """
    Проверка, что город удовлетворяет условию и выводит его
    :param AI_city:город ИИ
    :param cities: сет городов
    :return:
    """
    cities.discard(AI_city)
    print(f"Компьютер назвал город {AI_city}")
    return cities


def hum_win() -> None:
    """
    Скорее бесполезная функция, которая выводится при условии, что ИИ не нашёл город
    :return:
    """
    print('Вы победили!')


main(turn, cities_names)
