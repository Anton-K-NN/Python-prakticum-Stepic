'''
На вход подаётся строка, некоторые слова в которой "испорчены".

Признак "испорченного" слова - 1я буква в нём заменена на *.

Выведете на печать только "не испорченные" слова, каждое с новой строки

Sample Input:

exaggeration *romotion run into admit exactly *idelity *erspective treat check certain
Sample Output:

exaggeration
run
into
admit
exactly
treat
check
certain
'''

a=input().split()
s=[]
for x in a:
    if x[0]=='*':
        s.append(a.index(x))
k=0
for z in s:
    a.pop(int(z-k))
    k+=1
for c in a:
    print(c)

