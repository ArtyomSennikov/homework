# Задача "Банковские операции":
# Создать класс Bank со следующими свойствами:
# Атрибуты объекта:
# 1. balance - баланс банка (int).
# 2. lock - объект класса Lock для блокировки потоков.
# Методы объекта:
# 1. Метод deposit:
# Будет совершать 100 транзакций пополнения средств.
# Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
# Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
# После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
# Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
# 2. Метод take:
# Будет совершать 100 транзакций снятия.
# Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
# В начале должно выводится сообщение "Запрос на <случайное число>".
# Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие,
# уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
# Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств"
# и заблокировать поток методом acquire.


import threading
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            i = randint(50, 500)
            self.balance += i
            print(f'Пополнение счёта на {i}. Текущий баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            i = randint(50, 500)
            print(f'Запрос на сумму {i}.')
            if self.balance >= i:
                self.balance -= i
                print(f'Снятие: {i}. Текущий баланс: {self.balance}.')
                sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')