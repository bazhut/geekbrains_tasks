import random


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"I`m {self.name}, car color is {self.color}, car go, I`m drive a police car - {self.is_police}.")

    def stop(self):
        print(f"I`m {self.name}, car color is {self.color}, car stopped.")

    def turn(self, direction):
        print(f"I`m {self.name}, car color is {self.color}, car turn {'right' if direction == 'right' else 'left'}.")

    def show_speed(self):
        print(f"I`m {self.name}, car color is {self.color}, car speed is {self.speed}km/h.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Воу гоньщик, сбавь, ты в городе!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Воу гоньщик, сбавь, ты на рабочей машине!")


class SpeedCar(Car):
    def __init__(self, name, color, speed, max_speed, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.max_speed = max_speed

    def go_max(self):
        self.speed = self.max_speed
        print(self.speed)

    def slow_down(self):
        self.speed = 60
        print(self.speed)


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

    def police_siren(self):
        print(f"I`m {self.name} and i turn on my siren")


car = Car("Dick", "Green", 65)
car.show_speed()
town_car = TownCar("Dick", "Yellow", 65)
town_car.show_speed()
speed_car = SpeedCar("Rick", "Red", 160, 320)
speed_car.go_max()
speed_car.slow_down()
police_car = PoliceCar("Sam", "Black", 90, True)
police_car.police_siren()
police_car.go()
police_car.turn("left")
