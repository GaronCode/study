#Набор функций для работы с многочленом в строчном представлении

def open_file(path, p = 'r'):
    try: 
        f = open(path, p)
    except IOError:
        print('Файл '+FILE_NAME+' не существует!')
        return False
    else:
        return f







# Специальное преобразование в тип данных int с дополнительным условием - пустую строку приравнивать к единице
def sup_int(i):
    if i =='':
        return 1
    return int(i)

# Преобразует строку в "удобный" многочлен
def make_mch_list(str):
    list = {}
    tmp = str.split()
    z = 1
    for i in tmp:
        z = 1
        if i == "+":
            continue
        elif i == "-":
            z = -1
            continue
        a = i.split('x')
        if len(a) == 1:
            if 0 in list:
                list[0] += int(a[0])
            else:
                list[0] = int(a[0])
            continue
        elif len(a) == 2:
            list[sup_int(a[1][1:])] = sup_int(a[0]) * z
        else:
            print('Ошибка парсинга')
            break
    return list

# Печатает многочлен с типом "удобный" в человекопонятном виде
def print_mch(mch):
    
    text = ''
    for ex in mch:
        multi = mch[ex]
        unit = ''
        if ex == 0:
            unit = str(multi)
        else:
            if ex == 1:
                t = "x"
            else:
                t = "x^" + str(ex)
            unit = str(multi) + t
        
        if multi >= 0:
            t = " + "
        else:
            t = " - "
        unit = t + unit
        text += unit
    return text[3:]

# суммирует два "удобных" многочлена
def sum_mch(mch1, mch2):
    list = {}
    def add(mch):
        for i in mch:
            if i in list:
                list[i] += mch[i]
            else:
                list[i] = mch[i]
    add(mch1)
    add(mch2)
    return list


f1 = make_mch_list(open_file('mch_1.txt').read())
f2 = make_mch_list(open_file('mch_2.txt').read())

print(print_mch(f1))
print(print_mch(f2))

print(print_mch(sum_mch(f1,f2)))