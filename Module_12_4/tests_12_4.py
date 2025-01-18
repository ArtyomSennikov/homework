# Задача "Логирование бегунов".
#
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub.
# Основное обновление - выбрасывание исключений, если передан неверный тип в name и
# если передано отрицательное значение в speed.
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.

# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
# 1. Уровень - INFO.
# 2. Режим - запись с заменой('w').
# 3. Название файла - runner_tests.log
# 4. Кодировка - UTF-8
# 5. Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
# 1. Оберните основной код конструкцией try-except.
# 2. При создании объекта Runner передавайте отрицательное значение в speed.
# 3. В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# 4. В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".

# test_run:
# 1. Оберните основной код конструкцией try-except.
# 2. При создании объекта Runner передавайте что-то кроме строки в name.
# 3. В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# 4. В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".

import logging
import unittest
import rt_with_exceptions as rtwe


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            walker_ = rtwe.Runner('Name', -5)
            for i in range(10):
                walker_.walk()
            self.assertEqual(walker_.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner_ = rtwe.Runner('Name', 'Champion')
            for i in range(10):
                runner_.run()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')