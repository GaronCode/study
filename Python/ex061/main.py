import random as r
import lib

GROUPS = r.randint(2,5)


groups = [lib.Group(r.randint(20,30), lambda x: lib.Student(x, r.randint(30, 100)), i) for i in range(1, GROUPS+1)]

aver_score = [round(g.average_score(), 2) for g in groups]

print('Средний балл групп:',aver_score)


# не придумал как лаконичней сделать, решил "в лоб"
max_score = 0
id = 0
for i in aver_score:
    if i >= max_score:
        max_score = i
        max_score_obj = groups[id]
    id+=1

print('Максимальный бал:', max_score_obj.full_name())

