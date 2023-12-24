class smart_device:
    name = ''

    def __init__(self, name_dev: str):
        self.name = name_dev

    def turn_on(self):
        self.status = True

    def Turn_off(self):
        self.status = False

    def check_status(self):
        print(f'Состояние {self.name} сейчас {self.status}')


class important_message:
    def send_message(self, message: str):
        print(message)


class connection_to_wifi:
    def connect(self, wifi_name: str, password: str):
        print(f'Устройство было подключено к сети {wifi_name} с паролем {password}')


class schedule:
    schedule_dict = dict()

    def change_schedule(self, new_schedule: dict):
        self.schedule_dict = new_schedule


class smart_lamp(smart_device, connection_to_wifi):
    brightness = int()

    def change_brightness(self, count: int):
        self.brightness = count
        print(f'Яркость установлена на {self.brightness}')


class smart_smoke_detector(smart_device, important_message, connection_to_wifi):
    status = bool()

    def check_for_smoke(self):
        if self.status:
            return True
        else:
            return False


class smart_humidifier(smart_device, connection_to_wifi, schedule):
    humidity_level = int()

    def humidity_level_changer(self, count: int):
        self.humidity_level = count
        print(f'Влажность установлена на {self.humidity_level}')


lamp = smart_lamp('Кабинет')
smoker = smart_smoke_detector('Кухня')
hum = smart_humidifier('Спальня')

lamp.connect('wifi-home', '12963587')
hum.connect('wifi-home', '12963587')

lamp.turn_on()
hum.turn_on()
smoker.turn_on()

lamp.change_brightness(50)
hum.humidity_level_changer(45)

hum.change_schedule({'08:00': 'On', '22:00': 'Off'})

lamp.check_status()
smoker.check_status()
hum.check_status()

if smoker.check_for_smoke():
    smoker.send_message('Обнаружен дым на кухне')