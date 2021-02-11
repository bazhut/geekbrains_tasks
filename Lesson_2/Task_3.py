# List
month_inp = input("Type number of month: ")
month_list = ["Jan", "Feb", "Mar", "Apr", "May", "June",
              "Jule", "Aug", "Sept", "Oct", "Nov", "Dec"]
if month_inp.isnumeric():
    month_inp = int(month_inp)
    if 0 < month_inp <= 12:
        print(f"Вы выбрали месяц под названием {month_list[month_inp - 1]}")
    else:
        print("Введи число от 1 до 12!")
else:
    print("Введите число!")

# Dict
month_inp = input("Type number of month: ")
month_dict = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "June",
              7: "Jule", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec"}
if month_inp.isnumeric():
    month_inp = int(month_inp)
    if 0 < month_inp <= 12:
        print(f"Вы выбрали месяц под названием {month_dict.get(month_inp)}")
    else:
        print("Введи число от 1 до 12!")
else:
    print("Введите число!")

