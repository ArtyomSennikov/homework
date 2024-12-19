# Задача "Потоковая запись в файлы":
# Создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
# с прерыванием после записи каждого на 0.1 секунду.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

import threading
from time import sleep
from time import time

start_1 = time()

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf_8') as file:
        for i in range(word_count):
            sleep(0.1)
            file.write(f'Какое-то слово № {i + 1}\n')
    return print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_1 = time()
print(f'Работа функций: {round(end_1 - start_1, 2)} секунд(ы)')

start_2 = time()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

end_2 = time()
print(f'Работа потоков: {round(end_2 - start_2), 2} секунд(ы)')