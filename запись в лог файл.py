'''
event - переменная с текстом события
file_name - имя файла с логом
Файл с логом содержит записи о некоторых событиях вида:

event 3 - 'git log -2'
event 2 - 'git log'
event 1 - 'git status'
Пример нового события:

git fetch origin
Дополните лог в файле так, чтобы новое событие было записано вверху. Не забудьте указать порядковый номер события.

event 4 - 'git fetch origin'
event 3 - 'git log -2'
event 2 - 'git log'
event 1 - 'git status'
Если файл отсутствует или не содержит записей, начните нумеровать события с 1.

Не забывайте про переносы строк!
'''
import os.path
event='\''+event+'\''
if os.path.isfile(file_name):
    with open(file_name,'r') as file:
        text_file1=file.readlines()
        if text_file1==[]:
            numb1=0
        else:
            numb1=int((text_file1[0].split())[1])
    with open(file_name,'w') as file:
        text2='event ' + str(numb1+1) + ' - ' + event
        file.write(text2)
        file.write('\n')
    with open(file_name,'a') as file:
        for x in text_file1:
            file.write(x)
else:
    numb1=0
    with open(file_name,'w') as file:
        text2='event ' + str(numb1+1) + ' - ' + event
        file.write(text2)