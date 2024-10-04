# Практическое задание по теме неизменяемые объекты. Кортежи.
immutable_var = (1.0, 5, 'string', True) # создание кортежа данных
print(immutable_var)
#immutable_var[0]= 2 # выполнение этой строки кода приведёт к ошибке программы
mutable_list = [1.0, 5, 'string', True, False] # создание изменяемого списка данных
mutable_list[4] = True # изменение одного из значений в списке
print(mutable_list)