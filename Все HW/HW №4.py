number = input("Введите номер телефона: ")
checker = 0
number_checker = number
number_count = 0
m = 0
while m < 10:
    number_count += number.count(str(m))
    m += 1
if number_count == 11:
    checker += 1
if (number.find('8') == 0) or (number.find('7') == 1 and number.find('+') == 0):
    checker += 1
number_checker = number_checker.strip()
number_checker = number_checker.replace('0', '', 11)
number_checker = number_checker.replace('1', '', 11)
number_checker = number_checker.replace('2', '', 11)
number_checker = number_checker.replace('3', '', 11)
number_checker = number_checker.replace('4', '', 11)
number_checker = number_checker.replace('5', '', 11)
number_checker = number_checker.replace('6', '', 11)
number_checker = number_checker.replace('7', '', 11)
number_checker = number_checker.replace('8', '', 11)
number_checker = number_checker.replace('9', '', 11)
number_checker = number_checker.replace('+', '', 11)
number_checker = number_checker.replace(' ', '', 11)
number_checker = number_checker.replace('(', '', 11)
number_checker = number_checker.replace(')', '', 11)
number_checker = number_checker.replace('-', '', 11)
if number_checker == '':
    checker += 1
if checker == 3:
    print(f"Номер {number} прошёл проверку")
else:
    print(f"Номер {number} не прошёл проверку")
# -----------------------------------------------------------------------------------------
password = input("Введите пароль: ")
newchecker = 0
if len(password) > 7:
    newchecker += 1
if password.count(' ') == 0:
    newchecker += 1
if not (password.isupper() and password.islower()):
    newchecker += 1
if not password.isalnum():
    newchecker += 1
if newchecker == 4:
    print("Пароль надёжный")
else:
    print("Рекомендуем сменить пароль на более сложный")
