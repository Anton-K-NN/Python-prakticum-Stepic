'''
Напишите функцию wisdom_multiplication(x, y, length_check = True), реализующую умножение по схеме мудреца с прошлого шага.

Вычитаем из 100 первое и второе число.
Складываем результаты шага 1.
Вычитаем из 100 результат шага 2.
Перемножаем результаты шага 1.
Результат шага 3 даёт первые цифры результата, а результат шага 4 даёт последние 2 цифры результата.
В зависимости от значения аргумента length_check функция проверяет или нет длину результата шага 4 и при необходимости дописывает 0 перед ним (если результат всего 1 цифра).

Функция должна возвращать целое число.
'''

def multiplication_check_list(start=10, stop=99, length_check = True):
    n, m = 0, 0
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            s = 100 - ((100 - x) + (100 - y))
            k = (100 - x) * (100 - y)
            s = str(s)
            if length_check == True:
                if len(str(k)) == 1:
                    k = '0' + str(k)
                else:
                    k = str(k)
            else:
                k = str(k)
            ans = s + k
            if int(ans) == x * y:
                n += 1
            else:
                m += 1
    print('Правильных результатов:', n)
    print('Неправильных результатов:', m)

x,y=int(input()),int(input())
#print(wisdom_multiplication(x, y, length_check = False))
multiplication_check_list(x,y, length_check = True)