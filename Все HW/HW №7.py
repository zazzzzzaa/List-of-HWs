data_lst = ['1'
    ,
            '2'
    ,
            '3'
    ,
            '4d'
    , 5]

data_num = []

for num in data_lst:
    n = num
    try:
        num = int(num)
    except ValueError:
        print(f"{num} - невалидные данные")
        break
    data_num += n
print(data_num)
# ---------------------------------------------------------
number = input("Введите номер телефона: ")
checker = 0
number_checker = number
number_count = 0
m = 0
q = 0
while m < 10:
    number_count += number.count(str(m))
    m += 1
if number_count == 11:
    checker += 1
if (number.find('8') == 0) or (number.find('7') == 1 and number.find('+') == 0):
    checker += 1
number_checker = number_checker.strip()
while q < 10:
    number_checker = number_checker.replace(str(q), '', 11)
    q += 1
number_checker = number_checker.replace('+', '', 11)
number_checker = number_checker.replace(' ', '', 11)
number_checker = number_checker.replace('(', '', 11)
number_checker = number_checker.replace(')', '', 11)
number_checker = number_checker.replace('-', '', 11)
if number_checker == '':
    checker += 1
if number_count > 11:
    raise ValueError(f"В номере {number} более 11 символов")
elif number_count < 11:
    raise ValueError(f"В номере {number} менее 11 символов")
if (number.find('8') == 0) or (number.find('7') == 1 and number.find('+') == 0):
    q = 0
else:
    raise ValueError(f"Номер {number} начинается не с 8 или с +7")
if checker == 3:
    print(f"Номер {number} подходит")