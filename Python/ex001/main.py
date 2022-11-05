print('Программа для вывода списка факториалов от 1 до N включительно')
n = int(input("Введите N: "))

def list_of_factorials(l):
    i = 2
    s = [1]
    sum = 1
    while i <= l:
        sum *= i
        s.append(sum)
        i += 1
    return s
    
print(list_of_factorials(n))