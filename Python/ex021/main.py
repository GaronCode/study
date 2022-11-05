print("Программа для резделеия любого целого положительного числа на делители")
n = int(input("Введите целое положительное число: "))

ans = str(n) + " =>"
while n > 1:
    for i in range(2, n+1):
        if n%i == 0:
            n = int(n/i)
            ans += " "+str(i)
            break
print(ans)