'''
Реализуйте функцию caesar(text, key), возвращающую зашифрованный текст, работающую только с латинским алфавитом.

text - исходных текст, который надо зашифровать (или расшифровать)
key - ключ (сдвиг)
Ключ может быть отрицательным или больше 26

Из преобразуемого текста удаляются все пробелы и знаки препинания. Зашифрованный текст пишется в верхнем регистре 1 строкой.
'''
import re
def caesar(text,key):
    alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    t=text.upper().split()
    #print(t)
    tr=''.join(t)
    pattern = r"(\W)*"
    tr = re.sub(pattern,'',tr)
    #print(tr)
    ntr=''
    if key>0 and key < 26:
        alfkey = alf[key:] + alf[:key]
        # print(alfkey)
    elif key > 26 or key<-26:
        newkey = key%26
        alfkey = alf[newkey:] + alf[:newkey]
        #print(alfkey)
    elif key == 0 or key == 26:
        alfkey = alf
    elif key>-26 and key<0:
        newkey = 26+key
        alfkey = alf[newkey:] + alf[:newkey]

    for i in range(len(tr)):
        ntr=ntr + alfkey[alf.index(tr[i])]
        #print(ntr)
    return ntr

tex=input()
k=int(input())

print(caesar(tex, k, al))