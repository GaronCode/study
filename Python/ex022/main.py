FILE_NAME = 'icecream_store.txt'
try: 
    f = open(FILE_NAME, 'r', encoding="utf8")
except IOError:
    print('Файл со списком мороженного ('+FILE_NAME+') не существует!')
else:
    s = f.readlines()
    f.close()
    products_all = s[0][:-1].split(',')
    products_available = s[1][:-1].split(',')

    def not_available_list(all, available):
        not_avaliable = []
        for i in all:
            flag = True
            for j in available:
                if i == j:
                    flag = False
                    break
            if flag:
                not_avaliable.append(i)
        return not_avaliable
    
    def beautifier_list_str(list):
        i = 1
        text = ''
        for item in list:
            text += str(i)+". "+item+"\n"
            i += 1
        return text
    print('Отсутствует на складе:')
    print(beautifier_list_str(not_available_list(products_all, products_available)))