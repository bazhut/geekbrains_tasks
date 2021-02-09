time_inp = int(input("Введите время в секундах: "))
h = time_inp // 3600
m = (time_inp - h * 3600) // 60
s = time_inp % 60
print(f"{h:02}:{m:02}:{s:02}")
