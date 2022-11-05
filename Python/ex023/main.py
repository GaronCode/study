from decimal import *
import math
print("Программа для отбрасывания знаков после запятой числа Пи до указанного значения N")



# Имеется проблема с делением в двоичной системе. (например при вводе тройки)
# def roundDecToMin(i, z):
#     return math.floor(i * 10**z) * 10 ** (-z)

def roundDecToMin(i, z):
    a = str(i).split('.')
    return Decimal(a[0] + "." + a[1][:z])


print(roundDecToMin(math.pi, int(input("Введите число N: "))))