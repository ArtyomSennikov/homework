# Задача "План перехват":


# Написать 2 функции:
#
# Функция personal_sum(numbers):
# 1. Принимает коллекцию numbers.
# 2. Подсчитывает сумму чисел в numbers путём перебора и увеличивает переменную result.
# 3. Если при переборе встречается данное типа отличного от числового,
# то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
# 4. Функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.

# Функция calculate_average(numbers):
# 1. Принимает коллекцию numbers и возвращает: среднее арифметическое всех чисел.
# 2. Для подсчёта суммы использует функцию personal_sum написанную ранее.
# 3. Т.к. коллекция numbers может оказаться пустой,
# обрабатывает исключение ZeroDivisionError при делении на 0 и возвращает 0.
# 4. Также в numbers может быть записана не коллекция, а другие типы данных, например числа.
# Обработать исключение TypeError выводя строку 'В numbers записан некорректный тип данных'.
# В таком случае функция просто вернёт None.

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')

    return result, incorrect_data

def calculate_average(numbers):
    try:
        x, y = personal_sum(numbers)
        result = x / (len(numbers) - y)
        return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать