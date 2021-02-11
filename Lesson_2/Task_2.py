my_str = input("Type something using space: ")
my_list = list(my_str.split())
n = 0
for i in range(len(my_list)):
    if n + 1 < len(my_list):
        my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
        n += 2
    else:
        break

print(my_list)
