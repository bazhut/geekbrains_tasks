from abc import ABC, abstractmethod


class Clothes(ABC):
    total_exp = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        print(f"Затраты на пальто - {self.expense} м2")

    @property
    def expense(self):
        Clothes.total_exp += round(self.size / 6.5 + 0.5, 4)
        return round(self.size / 6.5 + 0.5, 4)


class Suite(Clothes):
    def __init__(self, height):
        self.height = height
        print(f"Затраты на костюм - {self.expense} м2")

    @property
    def expense(self):
        Clothes.total_exp += round(2 * self.height + 0.3, 4)
        return round(2 * self.height + 0.3, 4)


coat_1 = Coat(44)
print(Clothes.total_exp)
suite_1 = Suite(1.8)
print(Clothes.total_exp)
suite_2 = Suite(1.7)
print(Clothes.total_exp)
coat_2 = Coat(56)
print(Clothes.total_exp)
