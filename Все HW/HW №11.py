import json

with open('cities.json', 'r', encoding='utf-8') as file:
    cities_names = set(json.load(file))

turn = 0  # Это счётчик хода
checker_for_AI = 0  # необходимо, чтобы найти слово, начинающееся на нужную букву


def main(turn, checker, cities):
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
        AI_city, checker = city_AI(cities, city, checker)
        if checker == 1:
            AI_city, cities = city_AI_checker(AI_city, cities)
        else:
            hum_win()
            return 1


def city_hum():
    """
    Здесь человек вводит город и он записывается с большой буквы
    :return: возвращает город, выбранный человек после обработки
    """
    city = input("Введите название города РФ, оканчивающийся НЕ на ь/ъ/ы/ё, или остановите игру: ")
    city = city.title()
    return city


def city_hum_checker(city: str, cities):
    """
    Проверяет на остановку игры, находится ли слово в сете слов
    :param city: город, названный человеком
    :param cities: Все города
    :return:
    """
    if city in cities:
        return city
    elif city == 'Стоп' or city == 'стоп':
        print('Вы проиграли компьютеру :(')
        return False
    else:
        print("Такого города не существует или он уже был или он не удовлетворяет условию, вы проиграли")
        return False


def city_hum_del_for_turn_1(cities, city: str):
    """
    удаляет слово игрока на первом ходу
    :param cities: сет городов
    :param city: город игрока
    :return:
    """
    cities.discard(city)
    return cities


def city_AI(cities, city: str, checker: int):
    """
    Здесь выводим город ИИ
    :param cities: сет городов
    :param city: город игрока
    :param checker: счётчик для нахождения слова на нужную букву
    :return:
    """
    for name in cities:
        if name[0:1] == city[-1::].title():
            AI_city = name
            checker = 1
            return AI_city, checker


def city_AI_checker(AI_city, cities):
    """
    Проверка, что город удовлетворяет условию и выводит его
    :param AI_city:
    :param cities:
    :return:
    """
    cities.discard(AI_city)
    print(f"Компьютер назвал город {AI_city}")
    return AI_city, cities


def hum_win():
    """
    Скорее бесполезная функция, которая выводится при условии, что ИИ не нашёл город
    :return:
    """
    print('Вы победили!')
    return True


main(turn, checker_for_AI, cities_names)
