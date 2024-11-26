# Задача "Записать и запомнить"

# Создать функцию custom_write(file_name, strings), которая принимает аргументы
# file_name - название файла для записи,
# strings - список строк для записи.
# 1. Записать в файл file_name все строки из списка strings, каждая на новой строке.
# 2. Вернуть словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка.
# Для получения номера байта начала строки использовать метод tell() перед записью.

# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

# Ожидаемый вывод в консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')

def custom_write(file_name, strings):
    string_positions = {}
    a = 0
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        a += 1
        b = file.tell()
        file.write(i + '\n')
        string_positions[a, b] = i
    file.close()
    return string_positions


info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)