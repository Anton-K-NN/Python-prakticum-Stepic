'''
1. Предел функции
Реализуйте функцию f(x):

f(x) = 2arctg(x)
f(x)=2arctg(x)

Найдите предел функции (ответ округлите до 3 знака после запятой) при x\rightarrow +\inftyx→+∞

\lim_{x\rightarrow +\infty }2arctg(x)
x→+∞
lim
​
 2arctg(x)
Hint: Арктангенс доступен в модуле math под именем atan.
'''

import math
def f(x):
    return 2* math.atan(x)
lim = f(10000000)
print(round(lim,3))