import json

# from cities import cities_list
# cities_name_set = set()
# for city in cities_list:
#     if city['name'][-1].lower() not in 'ёьъы':
#         cities_name_set.add(city['name'])
# with open('cities.json', 'w', encoding='utf-8') as file:
#     json.dump(list(cities_name_set), file, ensure_ascii=False, indent=4)

with open('cities.json', 'r', encoding='utf-8') as file:
    cities_names = set(json.load(file))
turn = 0  # Это счётчик хода
checker_for_AI = 0  # необходимо, чтобы найти слово, начинающееся на нужную букву
# Постарался сделать код более читаемым, но от checker_for_AI не получилось избавиться
while cities_names != {}:
    city = input("Введите название города РФ, оканчивающийся НЕ на ь/ъ/ы/ё, или остановите игру: ")
    city = city.title()
    if city in cities_names:
        print()
    elif city == 'Стоп' or city == 'стоп':
        print('Вы проиграли компьютеру :(')
        break
    else:
        print("Такого города не существует или он уже был или он неудовлетворяет условию, вы проиграли")
        break
        print('Этот print для решения проблемы с break, не обращайте на него внимания')
    #     Если честно, до сих пор не понимаю почему тут без этого принта ломается код, был бы очень признателен если бы вы
    #     при проверке написали в чём же тут проблема

    if turn == 0:
        cities_names.discard(city)
    else:
        if city[0:1] == AI_city[-1::].title():
            cities_names.discard(city)
        else:
            print('Вы проиграли')
            break
    for name in cities_names:
        if name[0:1] == city[-1::].title():
            AI_city = name
            checker_for_AI = 1
            continue
    if checker_for_AI == 1:
        cities_names.discard(AI_city)
        print(f"Компьютер назвал город {AI_city}")
        print()
    else:
        print("Вы победили!")
        break
    checker_for_AI = 0
    turn += 1
