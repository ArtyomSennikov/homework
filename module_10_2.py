# Задача "За честь и отвагу!":
# Создать класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# 1. Атрибут name - имя рыцаря. (str)
# 2. Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# 1. При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# 2. Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# 3. В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# 4. По прошествии 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>...,
# осталось <кол-во воинов> воинов."
# 5. После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"

import time
import threading


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.counter = 0

    def battle(self, x, y):
        while y:
            time.sleep(1)
            self.counter += 1
            y = y - x
            print(f'{self.name} сражается {self.counter} дней, осталось {y} воинов.')

    def run(self):
        print(f'{self.name} на нас напали!')
        self.battle(self.power, 100)
        print(f'{self.name} одержал победу спустя {self.counter} дней (дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились.')