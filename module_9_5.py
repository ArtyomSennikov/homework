# Задача "Range - это просто":

# Создать пользовательский класс исключения StepValueError, который наследуется от ValueError.
# Наследования достаточно, класс оставьте пустым при помощи оператора pass.
#
# Создать класс Iterator, который обладает следующими свойствами:
# Атрибуты объекта:
# 1. start - целое число, с которого начинается итерация.
# 2. stop - целое число, на котором заканчивается итерация.
# 3. step - шаг, с которым совершается итерация.
# 4. pointer - указывает на текущее число в итерации (изначально start).
# Методы объекта:
# 1. __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
# В этом методе в первую очередь проверяется step на равенство 0.
# Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0').
# 2.__iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
# 3.__next__ - метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута
# step итерация завершится либо когда pointer станет больше stop, либо меньше stop. Учесть это при описании метода.

class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        result = self.pointer
        self.pointer += self.step
        return result

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')

except StepValueError:
    print('Шаг указан неверно')


iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()