class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = ""
        for i in self.matrix:
            my_str += f"{i[0]} {i[1]}\n"
        return my_str

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[0])):
                result[i].append(self.matrix[i][j] + other.matrix[i][j])
        my_str = ""
        for i in result:
            my_str += f"{i[0]} {i[1]}\n"
        return my_str


matrix_1 = Matrix([[10, 3], [6, 4], [9, 1]])
matrix_2 = Matrix([[7, 6], [2, 7], [5, 14]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
