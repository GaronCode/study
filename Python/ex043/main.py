#является ли дробь несократимой (только для делимого меньшего, чем делитель)
def is_irreducible_fractions(dividend,divisor):
    if dividend == 1 or dividend == 0:
        return True
    for i in range(2, dividend+1):
        if dividend%i == 0 and divisor%i==0:
            return False
    return True

l = []
S = 11
print("Вывод всех неправильных дробей, ограниченных знаминателем <= S и результатом выполнения дроби в диапозоне 0..1")
for i in range(1,S+1):
    for j in range(i+1,S+1):
        if is_irreducible_fractions(i,j):
            print(str(i) + ' / '+str(j))
