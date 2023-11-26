from marvel import full_dict
phase = {
    1: "Первая фаза",
    2: "Вторая фаза",
    3: "Третья фаза",
    4: "Четвёртая фаза",
    5: "Пятая фаза",
    6: "Шестая фаза"
}
phase_num = ''
phase_inp = input("Введите номер фазы (от 1 до 6): ")
if phase_inp.isdigit() == 0:
    raise TypeError("Необходимо ввести число")
elif int(phase_inp) > 6 or int(phase_inp) < 1:
    raise ValueError("Такой фазы не существует")
else:
    phase_num = phase.pop(int(phase_inp))
for num in full_dict:
    if (full_dict.get(num)).get('stage') == phase_num:
        print((full_dict.get(num)).get('title'))
