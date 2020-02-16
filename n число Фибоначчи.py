'''
Числа Фибоначчи
Напишите функцию fib(n), возвращающую n-е число Фибоначчи.

'''

x=int(input())
def fib(n):
    fibon=[0,1,1]
    for i in range(2, n+1):
        fibon.insert(i,(fibon[i-1] + fibon[i-2]))
    return fibon[n]
print(fib(x))