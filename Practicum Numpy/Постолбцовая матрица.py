'''
На вход подаётся 2 строки:

1-я строка содержит 2 натуральных числа: n, m
2-я строка содержит число k
Создайте матрицу размера n*m такую, что каждый её столбец содержит числа от k до k+n-1 (с шагом 1).

Ответ запишите в переменную Z
'''

import numpy as np
n, m  = map(int, input().split())
k=int(input())
Z=np.arange(k,k+n, dtype=float)
Z=np.array([Z]*m)
Z=Z.transpose()
print(Z)