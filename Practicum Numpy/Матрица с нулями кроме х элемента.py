'''
Считайте 2 числа:

n - размер Numpy вектора
x - координата элемента вектора, который должен быть равен 1. Остальные элементы вектора должны быть равны 0.
Сохраните вектор в переменную Z.

Примечание. В этой задаче не нужно ничего выводить на печать. Только создать вектор Z.
'''

import numpy as np
n,x=int(input()), int(input())
Z=np.zeros(n)
Z[x]=1
print(Z)