from typing import Callable
import csv

user_password = input('Введите пароль на проверку: ')
user_nickname = input('Введите никнейм на проверку: ')

# # Первое задание
#
# def password_checker(func: Callable) -> Callable:
#     def wrapper(pas: str) -> None:
#         check_for_num = False  # Штука на проверку цифр
#         check_for_sym = False  # Штука на проверку спец символов
#         if not (len(pas) >= 8):
#             raise ValueError('Ваш пароль слишком короткий')
#         if not (pas.lower() != pas):
#             raise ValueError('Ваш пароль не содержит заглавных букв')
#         if not (pas.upper() != pas):
#             raise ValueError('Ваш пароль не содержит строчных букв')
#         for i in pas:
#             if i in '0123456789':
#                 check_for_num = True
#             if i in '!"№;%:?*()_+@-#$^&-=`~\|/\[{]}<>,.':
#                 check_for_sym = True
#         if not check_for_num:
#             raise ValueError('Ваш пароль не содержит цифр')
#         if not check_for_sym:
#             raise ValueError('Ваш пароль не содержит спецсимволов')
#         func(pas)
#
#     return wrapper
#
#
# @password_checker
# def register_user(pas: str) -> None:
#     print(f'Ваш пароль {pas} прошёл проверку')
#
#
# register_user(user_password)


# Второе задание

def username_validator(func: Callable) -> Callable:
    def wrapper(pas: str, nickname: str) -> None:
        for i in nickname:
            if i == ' ':
                raise ValueError('В нике пользователя присутствует пробел')
        func(pas, nickname)

    return wrapper


def password_validator(func: Callable, min_len: int = 8, min_up: int = 1, min_low: int = 1,
                       min_spec_chairs: int = 1) -> Callable:
    def wrapper(pas: str, nickname: str) -> None:
        count_sym = 0  # счётчик спец символов
        count_lower = 0  # счётчик строчных букв
        count_upper = 0  # счётчик заглавных букв
        if not (len(pas) >= min_len):
            raise ValueError('Ваш пароль слишком короткий')
        for i in pas:
            if i.lower() == i:
                count_lower += 1
            if i.upper() == i:
                count_upper += 1
            if i in '!"№;%:?*()_+@-#$^&=`~\|/\[{]}<>,.':
                count_sym += 1
        if not (count_lower >= min_low):
            raise ValueError(f'Ваш пароль содержит меньше {min_low} строчных символов')
        if not (count_lower >= min_up):
            raise ValueError(f'Ваш пароль содержит меньше {min_up} строчных символов')
        if not (count_sym >= min_spec_chairs):
            raise ValueError(f'Ваш пароль содержит меньше {min_spec_chairs} спец. символов')
        username_validator(func(pas, nickname))

    return wrapper


@password_validator
@username_validator
def register_user_for_ex_2(pas: str, nickname: str) -> None:
    print('Регистрация прошла успешно')
    data = [pas, nickname]
    with open('user_data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)


register_user_for_ex_2(user_password, user_nickname)
