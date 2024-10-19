# Задание по распаковке позиционных параметров

def print_params (a=1, b='строка', c=True):
    print(a, b, c)

values_list = [1, 'Два', False]
values_dict = {'a': 1, 'b': 'str', 'c': True}
values_list_2 = [1.2, 'string']

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)