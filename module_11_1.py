# Домашнее задание по теме "Обзор сторонних библиотек Python".

import numpy as np

# Построение массива чисел от 1 до 9.
A = np.arange(1, 10)
print(A)

# Преобразование в матрицу 3х3.
A = A.reshape(3, 3)
print('\n', A)

# Изменение элементов матрицы через булев индексный массив.
I = np.array([[False, True, False], [True, False, True], [False, True, False]])
A[np.logical_not(I)] = 0
print('\n', A)