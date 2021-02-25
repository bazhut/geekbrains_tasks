from random import randint, random


with open("text_5.txt", "w") as f_obj:
    numbers = [el ** randint(5, 10) for el in range(1, 20)]
    print(numbers)
    for i in numbers:
        f_obj.writelines(f"{str(i)} ")

with open("text_5.txt", "r") as f_obj:
    sum_list = [int(el) for el in f_obj.read().split()]
    sum_ = sum(sum_list)
    print(sum_)
