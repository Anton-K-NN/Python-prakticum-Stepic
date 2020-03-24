'''
Считайте 3 числа:
n - количество элементов матрицы
m и l - размеры матрицы (число строк и столбцов соответственно)
Заполните матрицу Z числами от 0 до n-1 по порядку (сперва строки, потом столбцы).
Гарантируется, что m*l = n, т.е. все элементы "влезут" в матрицу и не останется пустых мест.

Примечание. В этой задаче не нужно ничего выводить на печать. Только создать матрицу Z.
'''

import numpy as np
n=int(input())
size=tuple(int(i) for i in input().split())
Z=np.arange(n).reshape(size)


print(Z)