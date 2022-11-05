import json
print('Примитивный чат-бот')
FILE_NAME = 'answers.json'
try: 
    f = open(FILE_NAME, 'r', encoding="utf8")
except IOError:
    print('Файл с ответами для чат бота ('+FILE_NAME+') Не существует!')
else:
    def answer(req, dict):
        from random import randint
        print(req)
        if req in dict['inputs']:

            if dict['inputs'][req] in dict['answers']:
                tmp = dict['answers'][dict['inputs'][req]]
                return tmp[randint(0,len(tmp)-1)]
        return dict["err"][randint(0, len(dict["err"])-1)]

    bot_answers = json.loads(f.read())
    f.close()
    req = ''
    print('Напишите боту "Пока" чтобы выйти. ')
    while 1:
        req = input('Напишите что-нибудь боту: ').lower()
        print(answer(req, bot_answers))
        if req == "пока":
            break
