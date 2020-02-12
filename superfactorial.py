'''
Напишите 2 функции:

для нахождения факториала числа factorial(n) = n!=1\cdot2\cdot3\cdot \ldots \cdot nfactorial(n)=n!=1⋅2⋅3⋅…⋅n
для нахождения суперфакториала числа - {\displaystyle \operatorname {sf} (n)=1!\cdot 2!\cdot 3!\cdot \ldots \cdot n!}sf(n)=1!⋅2!⋅3!⋅…⋅n!
Используйте функцию факториала для вычисления суперфакториала, чтобы сократить объём кода.
'''

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sf(n):
    s=1
    for x in range(n+1):
        s*=factorial(x)
    return s