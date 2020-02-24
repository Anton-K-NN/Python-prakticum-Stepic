'''
Реализуйте функцию caesar(text, key), возвращающую зашифрованный текст, работающую только с латинским алфавитом.

text - исходных текст, который надо зашифровать (или расшифровать)
key - ключ (сдвиг)
Ключ может быть отрицательным или больше 26

Из преобразуемого текста удаляются все пробелы и знаки препинания. Зашифрованный текст пишется в верхнем регистре 1 строкой.
'''
def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    t=text.upper().split()
    tr=''.join(t)
    #print(tr)
    ntr=''
    if len(alphabet)==0:
        return tr
    else:
        for i in range(len(tr)):
            if alphabet.find(tr[i]) != -1:
                # print('tr',tr[i])
                if (key > 0 and key < len(alphabet)) or (key > -len(alphabet) and key < 0):
                    ntr = ntr + alphabet[(alphabet.index(tr[i]) + key) % (len(alphabet))]
                elif key > len(alphabet):
                    newkey = (key) % len(alphabet)
                    ntr = ntr + alphabet[(alphabet.index(tr[i]) + newkey)]
                elif key < -len(alphabet):
                    newkey = -(abs(key) % len(alphabet))
                    ntr = ntr + alphabet[(alphabet.index(tr[i]) + newkey)]
                elif key == 0 or key == len(alphabet):
                    ntr = ntr + alphabet[alphabet.index(tr[i])]
            else:
                continue
            # print(ntr)
        return ntr


tex=input()
k=int(input())

print(caesar(tex, k))