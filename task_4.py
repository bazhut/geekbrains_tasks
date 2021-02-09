num = int(input("Введи число: "))
i = 0
while num / 10 > 1:
    if num % 10 > i:
        i = num % 10
        num = num // 10
    else:
        num = num // 10
        continue
print(i)
