'''
Пакетная проверка "схемы мудреца"
Пришла пора убедиться в том работает или нет схема. Для этого рассмотрим все пары двузначных чисел (от 10 до 99).

Чтобы задача была интереснее напишите универсальную функцию multiplication_check_list(start, stop), которая по умолчанию будет проверять весь интервал двузначных чисел (если никакие параметры не переданы), но так же позволит проверять и произвольные интервалы (например, от 15 до 20).

Гарантируется, что start НЕ БОЛЬШЕ stop.

Функция должна уметь печатать 2 строки:

Правильных результатов: n
Неправильных результатов: m
Примечание. Пары, где числа поменялись местами считаются РАЗНЫМИ.

Например, в интервале от 11 до 13 есть 9 пар:

11х11, 11х12, 11х13, 12х11, 12х12, 12х13, 13х11, 13х12, 13х13
'''

def multiplication_check_list(start=10, stop=99):
    n,m=0,0
    for x in range(start, stop+1):
        for y in range(start,stop+1):
            s=(100-((100-x)+(100-y)))*100+(100-x)*(100-y)
            if s==x*y:
                n+=1
            else:
                m+=1
    print('Правильных результатов:',n)
    print('Неправильных результатов:',m)


x,y=int(input()),int(input())
multiplication_check_list(x, y)