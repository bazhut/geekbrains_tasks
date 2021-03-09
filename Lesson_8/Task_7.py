class ComplexNum:
    def __init__(self, real, imag=0):
        self.complex_num = complex(real, imag)

    def __add__(self, other):
        return self.complex_num + other.complex_num

    def __mul__(self, other):
        return self.complex_num * other.complex_num


complex_1 = ComplexNum(3, 1)
complex_2 = ComplexNum(2, -3)
print(complex_1 * complex_2)
print(complex_1 + complex_2)
