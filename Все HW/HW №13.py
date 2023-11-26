from marvel import full_dict
from typing import Union, Dict
from pprint import pprint



# Не хотелось бы показаться душным, но если я правильно понял, то тут, в условии вашего задания, подразумеваются не
# цифры, а числа. Что может ввести в заблуждение.

# 2 Задание:

def is_int(str_num: str) -> Union[int, None]:
    if str_num.isdigit():
        str_num = int(str_num)
        return str_num
    else:
        return None


some_num = input('Введите числа через пробел: ')
some_num = list(map(is_int, some_num.split()))

# 3 Задание:

filtered_full_dict_by_id: dict = dict(filter(lambda num: num[0] in some_num, full_dict.items()))

# 4 Задание:

set_directors: set = {movie['director'] for movie in full_dict.values() if movie['director'] != 'TBA'}
pprint(set_directors)

# 5 Задание:

dict_years: Dict[int, Dict[str, str]] = {id: {'title': dict_id['title'],
                                              'year': str(dict_id['year']),
                                              'director': dict_id['director'],
                                              'screenwriter': dict_id['screenwriter'],
                                              'producer': dict_id['producer'],
                                              'stage': dict_id['stage']}
                                         for id, dict_id in full_dict.items()}

# pprint(dict_years, sort_dicts=False)

# 6 Задание:

filtred_dict_start: Dict[int, Dict[str, Union[str, int]]] = dict(
    filter(lambda word: word[1]['title'].startswith('Ч'), full_dict.items()))
pprint(filtred_dict_start, sort_dicts=False)

# 7 Задание. Фильтрую по первой фазе:

filtred_dict_by_phase_one: \
    Dict[int, Dict[str, Union[int, str]]] = dict(
    filter(lambda dict_1: dict_1[1]['stage'] == 'Первая фаза', full_dict.items()))

pprint(filtred_dict_by_phase_one, sort_dicts=False)

# 8 Задание. Фильтр по третьей фазе и первой букве в названии "М":

filtred_dict_by_two: Dict[int, Dict[str, Union[str, int]]] = dict(
    filter(lambda dict_2: dict_2[1]['title'].startswith('М') and dict_2[1]['stage'] == 'Третья фаза',
           full_dict.items()))

pprint(filtred_dict_by_two, sort_dicts=False)
