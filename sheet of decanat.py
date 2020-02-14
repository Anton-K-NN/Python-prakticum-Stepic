'''
5 из 15 шагов пройдено
2 из 6 баллов  получено
Представьте себя сотрудником деканата. Преподаватели предоставляют вам по 2 файла, имена которых находятся в переменных:

sheet - экзаменационную ведомость с фамилиями, именами и отчествами (если есть), оценками и статусами
mean - среднюю оценку по группе
Ведомость может выглядеть следующим образом:

Аттила 2 (экзамен)
Бонапарт Наполеон (неявка)
Гассан Абдуррахман ибн Хоттаб 5 (автомат)
Задойный Алексей Владимирович 5 (экзамен)
Колонна-Валевский Александр Флориан Жозеф (недопуск)
Цезарь Гай Юлий 4 (экзамен)
Последнее значение (в скобках) - статус:

экзамен - человек пришёл на экзамен и получил там оценку
автомат - человек хорошо учился и получил оценку "автоматом" до экзамена
неявка - человек не пришёл на экзамен и у него нет оценки
недопуск - человек не сдал зачёт по физкультуре, а потому его не допустили к нашему экзамену
Средняя оценка вычисляется только для тех, кто сдавал экзамен очно или получил автомат

Ваша задача считать данные по всем студентам из файла, вычислить средний балл и сравнить его с тем, что указал преподаватель в mean.

Если средний балл верен - напечатать "OK"

Если средний балл рассчитан с ошибкой - напечатать "ERROR"
'''

sheet=input()
mean-input()
f=open(sheet,'r', encoding="utf-8")
text_sheet=f.readlines()
s=0
i=0
for x in text_sheet:
   if x.find('(экзамен)')!=1 or x.find('(автомат)')!=1:
       qw=x.split()
       s+=int(qw[-2])
       i+=1
pritn(s)
d=open(mean,'r', encoding="utf-8")
text_mean=d.readlines()
sr=int(text_mean[0])
if (s/i)==sr:
    print('OK')
else:
    print("ERROR")
f.close()
d.close()