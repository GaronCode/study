from random import randint
from os import system


def create2dArr(x,y):
    return [[' '] * x for i in range(y)]

def printPole(y, target = {'x': 0, 'y': 0}):
    for iy,x in enumerate(y):
        td = ""
        ltd = ""
        for ix,item in enumerate(x):
            select1 = target['x'] == ix and target['y'] == iy
            select2 = target['x'] == ix+1 and target['y'] == iy
            select3 = target['x'] == ix and target['y'] == iy+1
            select4 = target['x'] == ix+1 and target['y'] == iy+1
            td += " " + item
            if iy+1 < len(y):
                ltd += ("━" if select1 or select3 else "─")*(len(item)+2)
                if ix+1 < len(x):
                    if select1:
                        ltd += "┩"
                    elif select2:
                        ltd += "╄"
                    elif select3:
                        ltd += "╅"
                    elif select4:
                        ltd += "╆"
                    else:
                        ltd += "┼"
            if ix+1 < len(x):
                if select1 or select2:
                    td += " ┃"
                else:
                    td += " │"
                
        print(td)
        print(ltd)


MAX_X = 2
MAX_Y = 2
pole = create2dArr(MAX_X+1,MAX_Y+1)

players = [{'type': 'player', 'symbol': "X", "name": "Игрок"},{'type': 'ai', 'symbol': "O", "name": "Бот"}]
nowTurnId = randint(0, len(players)-1)
target = {'x': 1, 'y': 1}


def nextTurn():
    global nowTurnId
    if nowTurnId >= len(players)-1:
        nowTurnId = 0
    else:
        nowTurnId += 1

def playerTurn(t, pole):
    global nowTurnId
    if pole[t['y']][t['x']] == " ":
        pole[t['y']][t['x']] = players[nowTurnId]['symbol']
        nextTurn()

def aiTurn():
    global pole
    allPosibleMoves = []
    for iy,itemY in enumerate(pole):
        for ix, itemX in enumerate(itemY):
            if itemX == " ":
                allPosibleMoves.append({"x": ix, "y": iy})
    move = allPosibleMoves[randint(0, len(allPosibleMoves)-1)]
    pole[move['y']][move['x']] = players[nowTurnId]['symbol']
    nextTurn()


while True:

    if players[nowTurnId]['type'] == 'ai':
        aiTurn()
        continue

    system('cls')
    printPole(pole, target)
    print('Сейчас ходит '+players[nowTurnId]['name'] + " c символом "+players[nowTurnId]['symbol'])
    print('Движение WASD,  (e - выход): ')
    i = input()
    
    
    if i == 'e':
        print('Выход')
        break;

    
    
    match i:
        case "w":
            if not(target['y'] == 0):
                target['y'] -= 1
        case "s":
            if not(target['y'] == MAX_Y):
                target['y'] += 1
        case "d":
            if not(target['x'] == MAX_X):
                target['x'] += 1
        case "a":
            if not(target['x'] == 0):
                target['x'] -= 1
        case " ":
            playerTurn(target, pole)
            continue

    

