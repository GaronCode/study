#Создание случайного списка, размером 10 элементов с их случайным значением диапазоне от 1 до 10
def random_list():
    from random import randint
    return [randint(1,10) for i in range(10)]

# Последовательности, начиная с первого элемента
def first_sequence(list, filter):
    prew_value = 0
    return [prew_value:=i for index,i in enumerate(list) if filter(i,prew_value) or index==0]

# Перебор всех последовательностей
def all_sequences(list, filter):
    all_seq = []
    for i in range(len(list)):
        a = first_sequence(list[i:], filter)
        all_seq.append(a) if len(a) > 1 else False
    return all_seq



l = random_list()
print(l)
# print('Первая возрастающая последовательность')
# print(first_sequence(l, lambda i,prew: i>prew))
# print('Последовательность первый элемент +1')
# print(first_sequence(l, lambda i,prew: i==prew+1))

print('Все возможные возрастающие последовательности')
print(all_sequences(l, lambda i,prew: i>prew))

print('Все возможные последовательности +1')
print(all_sequences(l, lambda i,prew: i==prew+1))