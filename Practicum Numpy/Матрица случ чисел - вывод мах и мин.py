'''
Считайте 2 числа: n, m.

Зафиксируйте значение генератора случайных чисел Numpy с помощью

numpy.random.seed(42)
Создайте матрицу n*m из случайных чисел (от 0 до 1).
Выведите на печать значение минимального и максимального чисел в получившейся матрице (каждое с новой строки).
'''
import numpy as np
np.random.seed(42)
size=tuple(int(i) for i in input().split())
#size =tuple(size)
print(size)
Z=np.random.random(size)
print(Z)
print(np.max(Z))
print(np.min(Z))