# Задача "Проверка на выносливость".

# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub.
# В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
# 1. test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
# Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта
# со значением 50.
# 2. test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
# Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта
# со значением 100.
# 3. test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
# Далее 10 раз у объектов вызываются методы run и walk соответственно.
# Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

# Пункты задачи:
# 1. Скачайте исходный код для тестов.
# 2. Создайте класс RunnerTest и соответствующие описанию методы.
# 2. Запустите RunnerTest и убедитесь в правильности результатов.

# Пример результата выполнения программы:
# Вывод на консоль:
# Ran 3 tests in 0.001s OK

import runner
from unittest import TestCase, main


class RunnerTest(TestCase):
    def test_walk(self):
        walker_ = runner.Runner('Name')
        for i in range(10):
            walker_.walk()
        self.assertEqual(walker_.distance, 50)

    def test_run(self):
        runner_ = runner.Runner('Name')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_challenge(self):
        walker_ = runner.Runner('Name1')
        runner_ = runner.Runner('Name2')
        for i in range(10):
            walker_.walk()
            runner_.run()
        self.assertNotEqual(walker_.distance, runner_.distance)

if __name__ == '__main__':
    main()