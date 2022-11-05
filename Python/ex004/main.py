print('Смещение рандомного списка на два элемента')

# Создание рандомного списка, с колличеством элементов n и рандомными числами от -rnd_range до rnd_range
def rnd_list_posiive_negative(n, rnd_range = 10):
    from random import randint
    rnd_list = []
    for i in range(n):
        rnd_list.append(randint(-rnd_range,rnd_range))
    return rnd_list;

# Смещение элементов списка list на shift позиций 
def shift_list(list, shift):
    for a in range(shift):
        list = list[-1:]+list[:-1]
    return list

# Пример использования:
N = 10
list = rnd_list_posiive_negative(N, N)
# выводим список
print(list)
# выводим смещённый список на два элемента
print(shift_list(list, 2))