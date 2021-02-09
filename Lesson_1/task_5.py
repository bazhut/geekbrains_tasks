vir = float(input("Введите выручки: "))
izd = float(input("Введите издержки: "))

if vir > izd:
    print("Profit!")
    ren = (vir - izd) / vir
    print(ren)
    empl = int(input("Кол-во работников: "))
    oneempl = (vir - izd) / empl
    print(oneempl)
else:
    print("Not profit!")

