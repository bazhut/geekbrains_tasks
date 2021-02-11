my_str = input("Введите несколько слов через пробел: ")
my_list = list(my_str.split())
for i, s in enumerate(my_list, 1):
    print(i, s[:10])
