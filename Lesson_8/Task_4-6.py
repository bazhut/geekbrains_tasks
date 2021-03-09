from abc import abstractmethod
from datetime import datetime


class Warehouse:
    def __init__(self, name_warehouse):
        self.name_warehouse = name_warehouse
        self.warehouse_dict = {'12': {'quantity': 24, 'price': 24.0, 'productivity': 12.0, 'type': 'Xerox'},
                               '33': {'quantity': 24, 'price': 24.0, 'productivity': 12.0, 'type': 'Xerox'}}
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


moscow_wh_1 = Warehouse("moscow_wh_1")
while True:
    try:
        answer_main = input("Добрый день! Что Вы хотите сделать?\n1. Добавить товар на склад\n"
                            "2. Отгрузить товар со склада\n3. Посмотреть остаток на складе\n"
                            "4. Посмотреть историю отгрузки\nДля выхода из программы введите 00.\n"
                            "Введите нужную цифру: ")
        if answer_main == "1":
            while True:
                try:
                    type_part = input("Какой тип товара Вы хотите добавить на склад?\n1. Принтер\n"
                                      "2. Сканер\n3. Ксерокс\nДля возврата назад введите 0\nВведите нужную цифру: ")
                    if type_part == "1":
                        while True:
                            try:
                                name = input("Введите название принтера: ").capitalize()
                                quantity = int(input("Введите количество: "))
                                price = float(input("Введите общую стоимость: "))
                                while True:
                                    try:
                                        color = input("Принтер цветной?\n1. Да\n2. Нет\nВведите нужную цифру: ")
                                        if color == "1":
                                            color = True
                                        elif color == "2":
                                            color = False
                                        else:
                                            raise MyOwnExc("Введите 1 или 2!")
                                    except MyOwnExc as err:
                                        print(err)
                                        continue
                                    else:
                                        while True:
                                            try:
                                                _ = input(
                                                    f"Проверьте введенные данные:\nНазвание принтера: {name}\n"
                                                    f"Количество: {quantity} шт.\nЦена общая: {price} р.\nПринтер "
                                                    f"{'цветной' if color else 'Ч/Б'}.\nДанные указаны верно?\n1. Да"
                                                    f"\n2. Нет\nВведите цифру: ")
                                                if _ == "1":
                                                    moscow_wh_1.add_to_warehouse(Printer(name, quantity, price, color))
                                                elif _ == "2":
                                                    raise MyMenuBack("Повторите ввод!")
                                                else:
                                                    raise MyOwnExc("Введите 1 или 2!")
                                            except MyOwnExc as err:
                                                print(err)
                                                continue
                                            else:
                                                break
                                    break
                            except ValueError:
                                print("Введите количество и сумму цифрами!")
                            except MyMenuBack as err:
                                print(err)
                                continue
                            else:
                                print("Партия товара добавлена на склад!")
                                break
                    elif type_part == "2":
                        while True:
                            try:
                                name = input("Введите название сканера: ").capitalize()
                                quantity = int(input("Введите количество: "))
                                price = float(input("Введите общую стоимость: "))
                                while True:
                                    try:
                                        wifi = input("Сканер с WiFi?\n1. Да\n2. Нет\nВведите нужную цифру: ")
                                        if wifi == "1":
                                            wifi = True
                                        elif wifi == "2":
                                            color = False
                                        else:
                                            raise MyOwnExc("Введите 1 или 2!")
                                    except MyOwnExc as err:
                                        print(err)
                                        continue
                                    else:
                                        while True:
                                            try:
                                                _ = input(
                                                    f"Проверьте введенные данные:\nНазвание сканера: {name}\n"
                                                    f"Количество: {quantity} шт.\nЦена общая: {price} р.\n"
                                                    f"Сканер с WiFi? {'да' if wifi else 'нет'}.\nДанные указаны верно?"
                                                    f"\n1. Да \n2. Нет\nВведите цифру: ")
                                                if _ == "1":
                                                    moscow_wh_1.add_to_warehouse(Scanner(name, quantity, price, wifi))
                                                elif _ == "2":
                                                    raise MyMenuBack("Повторите ввод!")
                                                else:
                                                    raise MyOwnExc("Введите 1 или 2!")
                                            except MyOwnExc as err:
                                                print(err)
                                                continue
                                            else:
                                                break
                                    break
                            except ValueError:
                                print("Введите количество и сумму цифрами!")
                            except MyMenuBack as err:
                                print(err)
                                continue
                            else:
                                print("Партия товара добавлена на склад!")
                                break
                    elif type_part == "3":
                        while True:
                            try:
                                name = input("Введите название ксерокса: ").capitalize()
                                quantity = int(input("Введите количество: "))
                                price = float(input("Введите общую стоимость: "))
                                productivity = float(input("Введите производительность ксерокса: "))
                                while True:
                                    try:
                                        _ = input(
                                            f"Проверьте введенные данные:\nНазвание ксерокса: {name}\n"
                                            f"Количество: {quantity} шт.\nЦена общая: {price} р.\n"
                                            f"Производительность ксерокса: {productivity}.\nДанные указаны верно?"
                                            f"\n1. Да \n2. Нет\nВведите цифру: ")
                                        if _ == "1":
                                            moscow_wh_1.add_to_warehouse(Xerox(name, quantity, price, productivity))
                                        elif _ == "2":
                                            raise MyMenuBack("Повторите ввод!")
                                        else:
                                            raise MyOwnExc("Введите 1 или 2!")
                                    except MyOwnExc as err:
                                        print(err)
                                        continue
                                    else:
                                        break
                            except ValueError:
                                print("Введите количество и сумму цифрами!")
                            except MyMenuBack as err:
                                print(err)
                                continue
                            else:
                                print("Партия товара добавлена на склад!")
                                break
                    elif type_part == "0":
                        break
                    else:
                        raise MyOwnExc("Ведите цифры от 0 до 3!")
                except MyOwnExc as err:
                    print(err)
                    continue
                except MyMenuBack as err:
                    continue
                else:
                    while True:
                        try:
                            answer_add = input("Хотите добавить еще партию?\n1. Да\n"
                                               "2. Нет\nВведите нужную цифру: ")
                            if answer_add == "1":
                                break
                            elif answer_add == "2":
                                raise MyMenuBack("")
                            else:
                                raise MyOwnExc("Введите цифры от 1 до 2!")
                        except MyOwnExc as err:
                            print(err)
                            continue
        elif answer_main == "2":
            pass
        elif answer_main == "3":
            for i in moscow_wh_1.warehouse_dict:
                print(f"Наименование товара: {i}, остаток на складе: "
                      f"{moscow_wh_1.warehouse_dict[i]['quantity']} шт."
                      f" сумма товаров: {moscow_wh_1.warehouse_dict[i]['price']} р.")
        elif answer_main == "4":
            pass
        elif answer_main == "00":
            print("До свидания!")
            break
        else:
            raise MyOwnExc("Введите цифру от 1 до 4!\nДля выхода введите 00.")
    except MyOwnExc as err:
        print(err)
    except MyMenuBack as err:
        continue
