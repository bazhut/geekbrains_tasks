def my_func(x, y):
    try:
        if x > 0 > y and float(y) == int(y):
            result = float(x) ** int(y)
            print(result)
        else:
            print("Args must be: x > 0 > y, y must be INT")
    except ValueError:
        print("Type a number!")


my_func(12, -3)


def my_func_for(x, y):
    try:
        if x > 0 > y and float(y) == int(y):
            i = 0
            num = x
            for i in range(abs(y) - 1):
                num *= x
                i += 1
            result = 1 / num
            print(result)
        else:
            print("Args must be: x > 0 > y, y must be INT")
    except ValueError:
        print("Type a number!")


my_func_for(12, -3)
