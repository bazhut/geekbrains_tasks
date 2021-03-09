class OnlyNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


num_list = []
print("Для остановки введите 'stop'")
while True:
    try:
        while True:
            inp_data = input("Введите число: ")
            if inp_data == "stop":
                break
            for i in inp_data.split():
                if is_number(i):
                    num_list.append(float(i))
                else:
                    raise OnlyNumbers("Only numbers, bro")
    except ValueError:
        print("Error!")
    except OnlyNumbers as err:
        print(err)
    else:
        print(num_list)
        break
