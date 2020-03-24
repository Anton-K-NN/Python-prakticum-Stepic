'''
Считайте 2 числа: n, m.

Зафиксируйте значение генератора случайных чисел Numpy с помощью

numpy.random.seed(42)
Создайте матрицу n*m из случайных чисел (от 0 до 1).
Найдите среднее значение для каждого из столбцов.
Выведите на печать значение минимального и максимального среднего по столбцам (каждое с новой строки).
import numpy as np
np.random.seed(42)
n, m  = map(int, input().split())
Z=np.random.random((n,m))
print(Z)
M=np.mean(Z, axis=0)
print(M)
print(np.min(M))
print(np.max(M))
#print(np.min(Z))