# Задание "Они все так похожи".

# Реализовать классы Figure (родительский), Circle, Triangle и Cube,
# объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированы и для них должны быть написаны
# интерфейсы взаимодействия (методы) - геттеры и сеттеры.

# Атрибуты класса Figure: sides_count = 0
# 1. Атрибуты (инкапсулированные): __sides (список сторон (целые числа)).
# __color(список цветов в формате RGB)
# 2. Атрибуты (публичные): filled (закрашенный, bool)

# 1. Метод get_color, возвращает список RGB цветов.
# 2. Метод __is_valid_color - служебный, принимает параметры r, g, b,
# проверяет корректность переданных значений перед установкой нового цвета.
# Корректный цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# 3. Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на
# соответствующие значения, предварительно проверив их на корректность.
# Если введены некорректные данные, то цвет остаётся прежним.
# 4. Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
# возвращает True если все стороны целые положительные числа и кол-во новых сторон
# совпадает с текущим, False - во всех остальных случаях.
# 5. Метод get_sides должен возвращать значение(я) атрибута __sides.
# 6. Метод __len__ должен возвращать периметр фигуры.
# 7. Метод set_sides(self, *new_sides) должен принимать новые стороны,
# если их количество не равно sides_count, то не изменять, в противном случае - менять.


# Атрибуты класса Circle: sides_count = 1
# 1. Все атрибуты и методы класса Figure.
# 2. Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# 3. Метод get_square возвращает площадь круга.
# Можно рассчитать как через длину, так и через радиус.


# Атрибуты класса Triangle: sides_count = 3
# 1. Все атрибуты и методы класса Figure.
# 2. Метод get_square возвращает площадь треугольника. (Можно рассчитать по формуле Герона).


# Атрибуты класса Cube: sides_count = 12
# 1. Все атрибуты и методы класса Figure.
# 2. Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона).
# 3. Метод get_volume, возвращает объём куба.


# Ожидаемые выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216


class Figure:
    sides_count = 0
    def __init__(self, color, sides):
        self.__color = color
        self.__sides = [sides] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if all(0 < i <= 255 and isinstance(i, int) for i in [r, g, b]):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if all(0 < i  and isinstance(i, int) for i in sides):
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides() == True:
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius ** 2



class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        for i in [self.get_sides()]:
            p = sum(i) / 2
            s = p * (p - i[0]) * (p - i[1]) * (p - i[2])
        return s


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
tr1 = Triangle((0, 0, 0), 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())