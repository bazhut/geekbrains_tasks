class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки с помощью инструмента {self.title}")


class Pen(Stationery):
    def draw(self):
        print("Draw with a pen!")


class Pencil(Stationery):
    def draw(self):
        print("Draw with a pencil!")


class Handle(Stationery):
    def draw(self):
        print("Draw with a Handle!")


pen_draw = Pen("pen")
pen_draw.draw()
draw = Stationery("Handle")
draw.draw()