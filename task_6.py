a = float(input("Результат пробежки в первый день?: "))
b = float(input("Сколько вы хотите пробежать?: "))
d = 1
while b > a:
    a = a * 1.1
    d += 1

print(f"На {d}-й день спортсмен достиг результата - не менее {b} км.")