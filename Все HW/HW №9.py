from cities import cities_list
n = 0
q = 0
m = 0
cities_names = set()
cities_name = set()
for numb in cities_list:
    cities_names.add(numb.get('name'))
for city_name in cities_names:
    if city_name[-1::] != 'ь' and city_name[-1::] != 'ъ' and city_name[-1::] != 'ы' and city_name[-1::] != 'ё':
        cities_name.add(city_name)
while cities_name != {}:
    city = input("Введите название города РФ, оканчивающийся НЕ на ь/ъ/ы/ё, или остановите игру: ")
    city = city.title()
    if city in cities_name:
        m += 1
    elif city == 'Стоп' or city == 'стоп':
        print('Вы проиграли компьютеру :(')
        break
    else:
        print("Такого города не существует или он уже был или он неудовлетворяет условию, вы проиграли")
        break
        print('Этот print для решения проблемы с break, не обращайте на него внимания')

    if n == 0:
        cities_name.discard(city)
    else:
        if city[0:1] == AI_city[-1::].title():
            cities_name.discard(city)
        else:
            print('Вы проиграли')
            break
    for name in cities_name:
        if name[0:1] == city[-1::].title():
            AI_city = name
            q = 1
            continue
    if q == 1:
        cities_name.discard(AI_city)
        print(f"Компьютер назвал город {AI_city}")
    else:
        print("Вы победили!")
        break
    q = 0
    n += 1
