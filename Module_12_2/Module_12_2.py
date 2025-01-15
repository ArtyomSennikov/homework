# Задача:
# Скачайте исходный код, который нужно обложить тестами с GitHub.
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.

# Изменения в классе Runner:
# 1. Появился атрибут speed для определения скорости бегуна.
# 2. Метод __eq__ для сравнивания имён бегунов.
# 3. Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.

# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников.
# Также присутствует метод start, который реализует логику бега по предложенной дистанции.

# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
# 1. setUpClass - метод, где создаётся атрибут класса all_results.
# Это словарь в который будут сохраняться результаты всех тестов.
# 2. setUp - метод, где создаются 3 объекта:
# а) Бегун по имени Усэйн, со скоростью 10.
# б) Бегун по имени Андрей, со скоростью 9.
# в) Бегун по имени Ник, со скоростью 3.
# 3. tearDownClass - метод, где выводятся all_results по очереди в столбец.
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
# У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу)
# и предполагаемое имя последнего бегуна.
# 4. Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
# а) Усэйн и Ник.
# б) Андрей и Ник.
# в) Усэйн, Андрей и Ник.
# Как можно понять: Ник всегда должен быть последним.

# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
# В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.

# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
# Ran 3 tests in 0.001s
# OK

import runner_and_tournament as rt
from unittest import TestCase, main


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = rt.Runner('Усейн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for key, value in value.items():
                res[key] = str(value)
            print(res)


    def test_run_1(self):
        run_1 = rt.Tournament(90, self.runner_1, self.runner_3)
        result = run_1.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_run_2(self):
        run_2 = rt.Tournament(90, self.runner_2, self.runner_3)
        result = run_2.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_run_3(self):
        run_3 = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = run_3.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    main()
