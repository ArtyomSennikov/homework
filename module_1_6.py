# Работа со словарями и множествами
my_dict = {'Kirill': 1995, 'Evgeny': 1989, 'Boris': 1991} # Создание словаря
print(my_dict)
print(my_dict.get('Boris')) # Обращение к одному из элементов в словаре по существующему ключу
print(my_dict.get('Alexey')) # Обращение к словарю по отсутствующему ключу
my_dict.update({'Anastasiya': 1990, 'Juliya': 1988}) # Добавление новых пар в словарь
print(my_dict)

my_set = {1, 2.5, 6, 2.5, 'True', (1, 2, 2.5), False, False} # Создание множества
print(my_set)
my_set.add(5) # Добавление нового элемента во множество
my_set.add ('String') # Добавление нового элемента во множество
my_set.discard((1, 2, 2.5)) # Удаление существующего элемента из множества
print(my_set)