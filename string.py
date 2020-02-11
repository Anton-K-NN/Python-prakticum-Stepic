'''
Напишите такую функцию counter(T):

принимающую на вход кортеж, состоящий из строк латинского алфавита, например, ("ABC", "abc")
приводящую строки к единому (верхнему, либо нижнему) регистру
определяющую число уникальных символов латинского алфавита для каждой строки (строка "Aaa" содержит всего 1 уникальный символ)
возвращающую длину строки с максимальным числом уникальных символов (если таких строк несколько, то самой длинной из них)
'''

def counter(T):
    f=[]
    for n in T:
        count={}
        for s in n.upper():
            if count.setdefault(s):
                count[s] += 1
            else:
                count[s] = 1
        f.append(len(count))
    print(f)
    print(max(f))
    print(f.index(max(f)))
    for d in f:
        print('d=',d)
        w=len(T[f.index(max(f))])
        if d==max(f) and f.index(d)<len(f)-2:
            ind=f.index(d,(f.index(max(f)))+1)
            print('ind=',ind)
            if len(T[f.index(max(f))])<len(T[ind]):
                w=len(T[ind])

    return w


x=('AAAaaa', 'ab')
print(counter(x))
