class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell - other.cell >= 0:
            return self.cell - other.cell
        else:
            return "less then 0!"

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return (self.cell + other.cell) // 2

    def make_order(self, len_row):
        my_str = ""
        a = 0
        for i in range(self.cell):
            my_str += "*"
            a += 1
            if a == len_row:
                my_str += "\n"
                a = 0
        return my_str


cell_1 = Cell(10)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2 // cell_1)
print(cell_1.make_order(4))