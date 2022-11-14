#Создание случайного списка, размером 10 элементов с их случайным значением диапазоне от 1 до 10
def random_list():
    from random import randint
    return [randint(1,10) for i in range(10)]

def count_in_first_seconds(f_list, s_list, filter = lambda x:True):
    l = {}
    for item in s_list:
        l[item] = 0
        for i in f_list:
            if item == i:
                l[item] += 1
    
    return {index: item for index,item in l.items() if filter(item)}


# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
print('Случайный список: ', l := random_list())
# print('Только уникальные элементы: ', l2 := list(dict.fromkeys(l)))
l2 = list(dict.fromkeys(l))
print('Список вхождений элементов списка в другой список: ')
print(l3 := count_in_first_seconds(l, l2, lambda x: x>1))




print('Колличество повторений')
z = 0
for i in l3:
    z +=l3[i]
print(z)

