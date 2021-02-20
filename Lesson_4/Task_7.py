from math import factorial


def fact(n):
    f_num = 1
    if n == 0:
        yield f"Factorial {n}! = 1"
    for i in range(1, n + 1):
        f_num *= i
        yield f"{i}! = {f_num}"


for el in fact(int(input("Type a number: "))):
    print(el)

