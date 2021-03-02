class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return f"{self._length} m * {self._width} m * 25 kg * 5 cm = {(self._length * self._width * 25 * 5) / 1000} ton"


same_road = Road(5000, 20)
print(same_road.mass())
