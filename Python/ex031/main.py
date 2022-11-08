#Создание случайного списка, размером 10 элементов с их случайным значением диапазоне от 1 до 10
def random_list():
    from random import randint
    return [randint(1,10) for i in range(10)]


#функция для фильтрации списка с помощью лямбда функции
def filter_list(list, filter):
    return [item for item in list if filter(item)]

# вывод отфильтрованного лямбда функцией списка 
print(filter_list(random_list(), lambda i: i>5))