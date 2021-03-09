class MyExpDevbyzero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    inp_num_1 = int(input("Введите делимое: "))
    inp_num_2 = int(input("Введите делитель: "))
    if inp_num_2 == 0:
        raise MyExpDevbyzero("Division by zero!")
except MyExpDevbyzero as e:
    print(e)
except ValueError:
    print("Вводите только числа!")
else:
    result = inp_num_1 / inp_num_2
    print(result)
