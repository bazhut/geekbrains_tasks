from random import randint


with open("text_5.txt", "w+") as f_obj:
    numbers = [randint(1, 10000) for _ in range(1000)]
    f_obj.write(' '.join([str(randint(1, 10000)) for _ in range(1000)]))
    f_obj.seek(0)
    print(sum(map(int, f_obj.readline().split())))
