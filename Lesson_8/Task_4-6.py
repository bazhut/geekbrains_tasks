from abc import abstractmethod
from datetime import datetime
import sys


class Warehouse:
    def __init__(self, name_warehouse):
        self.name_warehouse = name_warehouse
        self.warehouse_dict = {'Canon': {'quantity': 24, 'price': 240000, "color": True, 'type': 'Printer'},
                               'Epson': {'quantity': 45, 'price': 450000, 'wifi': 12.0, 'type': 'Scanner'},
                               'Nikon': {'quantity': 15, 'price': 150000, 'productivity': 12.0, 'type': 'Xerox'}}
        self.warehouse_transfer_history = {}

    def add_to_warehouse(self, *parts):
        for part in parts:
            if self.warehouse_dict.get(part.dict.get("name")) is None:
                self.warehouse_dict.update({part.dict.pop("name"): part.dict})
                return "На склад добавлена новая позиция!"
            else:
                self.warehouse_dict[part.dict.get("name")]["quantity"] = self.warehouse_dict[part.dict.get("name")][
                                                                             "quantity"] + part.dict["quantity"]
                self.warehouse_dict[part.dict.get("name")]["price"] = self.warehouse_dict[part.dict.get("name")][
                                                                          "price"] + part.dict["price"]
                return "Новая партия получена, данные обновлены!"

    def transfer_to(self, name_item, quantity_item, destination):
        if self.warehouse_dict.get(name_item) is None:
            return "На складе нет такой позиции!"
        else:
            if self.warehouse_dict[name_item]["quantity"] - quantity_item >= 0:
                before_price = self.warehouse_dict[name_item]["price"]
                self.warehouse_dict[name_item]["price"] -= \
                    self.warehouse_dict[name_item]["price"] / self.warehouse_dict[name_item]["quantity"] * quantity_item
                self.warehouse_dict[name_item]["quantity"] -= quantity_item
                if self.warehouse_transfer_history.get(datetime.now().strftime("%d.%m.%Y")) is None:
                    self.warehouse_transfer_history.update({datetime.now().strftime("%d.%m.%Y"): [
                        f"Партия - {name_item} в количестве {quantity_item}шт. на сумму "
                        f"{before_price - self.warehouse_dict[name_item]['price']} отправлена в {destination}\n"]})
                else:
                    return self.warehouse_transfer_history.get(datetime.now().strftime("%d.%m.%Y")).append(
                        f"Партия - {name_item} в количестве {quantity_item}шт. на сумму "
                        f"{before_price - self.warehouse_dict[name]['price']} отправлена в {destination}\n")
            else:
                return f"На складе находится только {self.warehouse_dict[name_item]['quantity']}ед. " \
                       f"товара - {name_item}, проверьте данные!"

    def check_dict(self, list_arg):
        args_dict = {2: "Printer", 3: "Scanner", 4: "Xerox"}
        args_list = []
        for arg in list_arg:
            if arg == 1:
                args_list_all = []
                for el in self.warehouse_dict.keys():
                    args_list_all.append(f'Наименование товара: {el}, остаток на складе: '
                                         f'{self.warehouse_dict[el]["quantity"]} шт., сумма товаров: '
                                         f'{self.warehouse_dict[el]["price"]} р.\n')
                return args_list_all
            for el in self.warehouse_dict.keys():
                if self.warehouse_dict[el]["type"] == args_dict[int(arg)]:
                    args_list.append(f'Наименование товара: {el}, остаток на складе: '
                                     f'{self.warehouse_dict[el]["quantity"]} шт., сумма товаров: '
                                     f'{self.warehouse_dict[el]["price"]} р.\n')
            return args_list


class OfficeEq:
    @abstractmethod
    def __init__(self, name_item, quantity_item, price_part):
        self.dict = {"name": name_item, "quantity": int(quantity_item), "price": float(price_part)}


class Printer(OfficeEq):
    def __init__(self, name_item, quantity_item, price_part, color_item):
        super().__init__(name_item, quantity_item, price_part)
        self.dict.update({"color": color_item, "type": Printer.__name__})


class Scanner(OfficeEq):
    def __init__(self, name_item, quantity_item, price_part, wifi_part):
        super().__init__(name_item, quantity_item, price_part)
        self.dict.update({"wifi": wifi_part, "type": Scanner.__name__})


class Xerox(OfficeEq):
    def __init__(self, name_item, quantity_item, price_part, productivity_part):
        super().__init__(name_item, quantity_item, price_part)
        self.dict.update({"productivity": productivity_part, "type": Xerox.__name__})


class MyOwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyMenuBack(Exception):
    def __init__(self, txt):
        self.txt = txt


def menu_atr(quantity_pos, answer, back="BACK", close="EXIT"):
    try:
        answer = int(answer)
    except ValueError:
        if answer.upper() == back:
            return back
        elif answer.upper() == close:
            return close
        else:
            num_list = [_ for _ in range(1, int(quantity_pos) + 1)]
            return f"Некорректный ввод! Введите число от {num_list[0]} до {num_list[-1]}."
    else:
        if int(quantity_pos) < int(answer) or int(answer) < 0:
            num_list = [_ for _ in range(1, int(quantity_pos) + 1)]
            return f"Некорректный ввод! Введите число от {num_list[0]} до {num_list[-1]}."
        else:
            return answer


moscow_wh_1 = Warehouse("moscow_wh_1")
while True:
    answer_main = input("Добрый день! Что Вы хотите сделать?\n1. Добавить товар на склад\n"
                        "2. Отгрузить товар со склада\n3. Посмотреть остаток на складе\n"
                        "4. Посмотреть историю отгрузки\nДля выхода из программы введите 'Exit'.\n"
                        "Введите нужную цифру: ")
    print("\n")
    answer_main_aft_check = menu_atr(4, answer_main)
    if answer_main_aft_check == 1:
        while True:
            type_part = input("Какой тип товара Вы хотите добавить на склад?\n1. Принтер\n"
                              "2. Сканер\n3. Ксерокс\nДля возврата назад введите 'Back'.\nВведите нужную цифру: ")
            print("\n")
            type_part_aft_check = menu_atr(3, type_part)
            if type_part_aft_check == 1:
                while True:
                    try:
                        name = input("Введите название принтера: ").capitalize()
                        quantity = int(input("Введите количество: "))
                        price = float(input("Введите общую стоимость: "))
                        while True:
                            color = input("Принтер цветной?\n1. Да\n2. Нет\nВведите нужную цифру: ")
                            print("\n")
                            color_aft_check = menu_atr(2, color)
                            if color_aft_check == 1:
                                color = True
                            elif color_aft_check == 2:
                                color = False
                            else:
                                print(color_aft_check)
                                continue
                            while True:
                                accept_inf = input(
                                    f"Проверьте введенные данные:\nНазвание принтера: {name}\n"
                                    f"Количество: {quantity} шт.\nЦена общая: {price} р.\nПринтер "
                                    f"{'цветной' if color else 'Ч/Б'}.\nДанные указаны верно?\n1. Да"
                                    f"\n2. Нет\nВведите цифру: ")
                                print("\n")
                                accept_inf_aft_check = menu_atr(2, accept_inf)
                                if accept_inf_aft_check == 1:
                                    print(moscow_wh_1.add_to_warehouse(Printer(name, quantity, price, color)))
                                    break
                                elif accept_inf_aft_check == 2:
                                    accept_err = input('Хотите ввести еще раз?\n 1. Да\n 2. Нет\nВведите цифру: ')
                                    print("\n")
                                    accept_err_aft_check = menu_atr(2, accept_err)
                                    while True:
                                        if accept_err_aft_check == 1:
                                            raise MyMenuBack("Повторите ввод!")
                                        elif accept_err_aft_check != 2 and accept_err_aft_check != 1:
                                            print(accept_err_aft_check)
                                            continue
                                        break
                                    break
                                else:
                                    print(accept_inf_aft_check)
                                    continue
                            del accept_inf, accept_inf_aft_check
                            break
                    except ValueError:
                        print("Введите количество и сумму цифрами!")
                    except MyMenuBack as err:
                        print(err)
                        continue
                    else:
                        break

            elif type_part_aft_check == 2:
                while True:
                    try:
                        name = input("Введите название сканера: ").capitalize()
                        quantity = int(input("Введите количество: "))
                        price = float(input("Введите общую стоимость: "))
                        while True:
                            wifi = input("Сканер с WiFi?\n1. Да\n2. Нет\nВведите нужную цифру: ")
                            print("\n")
                            wifi_aft_check = menu_atr(2, wifi)
                            if wifi_aft_check == 1:
                                wifi = True
                            elif wifi_aft_check == 2:
                                color = False
                            else:
                                print(wifi_aft_check)
                                continue
                            while True:
                                accept_inf = input(
                                    f"Проверьте введенные данные:\nНазвание сканера: {name}\n"
                                    f"Количество: {quantity} шт.\nЦена общая: {price} р.\n"
                                    f"Сканер с WiFi? {'да' if wifi else 'нет'}.\nДанные указаны верно?"
                                    f"\n1. Да \n2. Нет\nВведите цифру: ")
                                print("\n")
                                accept_inf_aft_check = menu_atr(2, accept_inf)
                                if accept_inf_aft_check == 1:
                                    print(moscow_wh_1.add_to_warehouse(Scanner(name, quantity, price, wifi)))
                                    break
                                elif accept_inf_aft_check == 2:
                                    accept_err = input('Хотите ввести еще раз?\n 1. Да\n 2. Нет\nВведите цифру: ')
                                    print("\n")
                                    accept_err_aft_check = menu_atr(2, accept_err)
                                    while True:
                                        if accept_err_aft_check == 1:
                                            raise MyMenuBack("Повторите ввод!")
                                        elif accept_err_aft_check != 2:
                                            print(accept_err_aft_check)
                                            continue
                                        break
                                    break
                                else:
                                    print(accept_inf_aft_check)
                                    continue
                            del accept_inf, accept_inf_aft_check
                            break
                    except ValueError:
                        print("Введите количество и сумму цифрами!")
                    except MyMenuBack as err:
                        print(err)
                        continue
                    else:
                        break
            elif type_part_aft_check == 3:
                while True:
                    try:
                        name = input("Введите название ксерокса: ").capitalize()
                        quantity = int(input("Введите количество: "))
                        price = float(input("Введите общую стоимость: "))
                        productivity = float(input("Введите производительность ксерокса: "))
                        print("\n")
                        while True:
                            accept_inf = input(
                                f"Проверьте введенные данные:\nНазвание ксерокса: {name}\n"
                                f"Количество: {quantity} шт.\nЦена общая: {price} р.\n"
                                f"Производительность ксерокса: {productivity}.\nДанные указаны верно?"
                                f"\n1. Да \n2. Нет\nВведите цифру: ")
                            print("\n")
                            accept_inf_aft_check = menu_atr(2, accept_inf)
                            if accept_inf_aft_check == 1:
                                print(moscow_wh_1.add_to_warehouse(Xerox(name, quantity, price, productivity)))
                                break
                            elif accept_inf_aft_check == 2:
                                accept_err = input('Хотите ввести еще раз?\n 1. Да\n 2. Нет\nВведите цифру: ')
                                print("\n")
                                accept_err_aft_check = menu_atr(2, accept_err)
                                while True:
                                    if accept_err_aft_check == 1:
                                        raise MyMenuBack("Повторите ввод!")
                                    elif accept_err_aft_check != 2:
                                        print(accept_err_aft_check)
                                        continue
                                    break
                                break
                            else:
                                print(accept_inf_aft_check)
                                continue
                        del accept_inf, accept_inf_aft_check
                    except ValueError:
                        print("Введите количество и сумму цифрами!")
                    except MyMenuBack as err:
                        print(err)
                        continue
                    else:
                        break
            elif type_part_aft_check == "BACK" or "EXIT":
                break
            else:
                print(type_part_aft_check)
                continue
            while True:
                answer_add = input("Хотите добавить еще партию?\n1. Да\n"
                                   "2. Нет\nВведите нужную цифру: ")
                print("\n")
                answer_add_aft_check = menu_atr(2, answer_add)
                if answer_add_aft_check != 1 and answer_add_aft_check != 2:
                    print(answer_add_aft_check)
                    continue
                break
            if answer_add_aft_check == 1:
                continue
            elif answer_add_aft_check == 2:
                break

    elif answer_main_aft_check == 2:
        pass
    elif answer_main_aft_check == 3:
        while True:
            try:
                dict_answ = input('Что Вас интересует?\n1. Весь остаток на складе.\n2. Остаток принтеров.\n'
                                  '3. Остаток сканеров.\n4. Остаток ксероксов.\n'
                                  'Вы можете ввести несколько цифр через пробел, для выхода введите "Back": ')
                print("\n")
                if dict_answ.upper() == "BACK":
                    break
                dict_answ_list = dict_answ.split()
                dict_set = set()
                for i in dict_answ_list:
                    i = int(i)
                    if 0 < i <= 4:
                        i = int(i)
                        dict_set.add(i)
                    else:
                        raise MyOwnExc("Введите число или набор чисел от 1 до 4!")
                dict_data = moscow_wh_1.check_dict(list(dict_set))
                if dict_data is None:
                    raise MyOwnExc("Введите число или набор чисел от 1 до 4!")
            except ValueError:
                print("Вводите только цифры через пробел!")
            except MyOwnExc as er:
                print(er)
                continue
            else:
                for i in dict_data:
                    print(i, end="")
                input("Для продолжения нажмите Enter. ")
                print("\n")
                while True:
                    dict_check = input("Хотите посмотреть еще что-то на складе?\n1. Да\n"
                                       "2. Нет\nВведите нужную цифру: ")
                    print("\n")
                    dict_check_aft_check = menu_atr(2, dict_check)
                    if dict_check_aft_check != 1 and dict_check_aft_check != 2:
                        print(dict_check_aft_check)
                        continue
                    break
                if dict_check_aft_check == 1:
                    continue
                break
    elif answer_main_aft_check == 4:
        pass
    elif answer_main_aft_check == "EXIT":
        print("До свидания!")
        sys.exit()
    else:
        print(answer_main_aft_check)
        continue
