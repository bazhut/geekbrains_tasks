class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


worker = Position("Sam", "Smith", "Worker", 1000, 522)
print(worker.get_full_name())
print(worker.get_total_income())
worker_1 = Position("Joe", "Kek", "Worker_1", 920, 325)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
