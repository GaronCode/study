# Определеие числа Фибоначчи для числа n
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

# Функция возвращает строку со списком чисел Фибоначчи от 0 до n
def fib_str(n):
    if n > 0:
        text = ''
        for x in range(n):
            text += str(F(x+1)) + ' '
    return text
        
# Программа для записи/перезаписи любого текста (text) в файл (file_name)
def write_to_file(text, file_name = 'fib.txt'):
    file = open(file_name, 'w+')
    file.write(text)
    file.close()
    print('Успешно!')

#Программа для записи чисел Фибоначчи от 0 до n в файл "fib.txt" в одну строку
n = int(input("Введите число N: "))
write_to_file(fib_str(n))