def division():
    while True:
        try:
            num_1 = float(input("Number 1: "))
            num_2 = float(input("Number 2: "))
            div = num_1 / num_2
            return print(round(div, 5))
        except ZeroDivisionError:
            print("Error! Division by zero!")
        except ValueError:
            print("Error! Type only numbers!")


division()
