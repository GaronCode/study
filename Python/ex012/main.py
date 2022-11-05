print('Программа для вывода всех фруктов из файла, начинающихся на выбранную букву')
FILE_NAME = 'fruits.txt'
try: 
    f = open(FILE_NAME, 'r', encoding="utf8")
except IOError:
    print('Файл с фруктами ('+FILE_NAME+') не существует!')
else:
    letter = input("Введите букву: ").lower()
    if 0 < len(letter) < 2:
            fruits_list = f.readlines()
            f.close()
            answer = ''
            for fruit in fruits_list:
                if fruit[0].lower() == letter:
                    answer += fruit
            if answer == '':
                print('Нет фруктов, начинающихся на букву '+letter)
            print(answer)
    else:
        print('Вы должны ввести только одну букву')