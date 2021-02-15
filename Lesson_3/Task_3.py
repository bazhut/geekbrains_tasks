def my_func(num_1, num_2, num_3):
    try:
        num = [num_1, num_2, num_3]
        num.remove(min(num))
        result = sum(num)
        print(result)
    except TypeError:
        print("Arg must be a number!")


my_func(1, 1, 1)
