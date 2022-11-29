import random as r
import lib
SIZE = 3
RANGE = [-100, 100]

matrix = [[r.randint(*RANGE) for x in range(SIZE)] for x in range(SIZE)]




lib.print_matrix(matrix)

sum_lines = []

sum_diag = 0
diag = [0,0]
for y, x_list in enumerate(matrix):
    sum_line = 0
    for x, x_element in enumerate(x_list):
        sum_line += x_element
        if x == diag[0] and y == diag[1]:
            diag[0]+=1
            diag[1]+=1
            sum_diag += x_element



    sum_lines.append(sum_line)

print('Суммы линий: ', sum_lines)
print('Сумма по диагонали: ', sum_diag)



big_lines = [key for key, item in enumerate(sum_lines) if item > sum_diag]
print('У строк под номерами ',big_lines,' сумма элеметров превосходит сумму по главной диагонали')

