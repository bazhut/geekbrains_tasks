from itertools import count, cycle


def cycle_func(some_list):
    p = 0
    for k in cycle(some_list):
        if p < 10:
            print(k)
            p += 1
        else:
            break


def count_func(num):
    for i in count(num):
        if i < num + 10:
            print(i)
        else:
            break


cycle_func("hbdhhdikic")

count_func(10)
