from functools import reduce


def mul_list(num_1, num_2):
    return num_1 * num_2


my_list = [el for el in range(100, 1001, 2)]
print(f"List\n{my_list}\nMultiplication of numbers:\n{reduce(mul_list, my_list)}")
