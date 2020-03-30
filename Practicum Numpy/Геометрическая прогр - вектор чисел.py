'''
На вход подаются 3 числа (каждое с новой строки):

start
stop
n
Составьте список из n точек на отрезке [start, stop] в геометрической прогрессии, включая start и stop.

Округлите значения точек до 3 знака после запятой.

Результат сохраните в переменную Z.
'''

import numpy as np
start=int(input())
stop=int(input())
n=int(input())
Z=np.geomspace(start,stop, num=n)
print(Z)
