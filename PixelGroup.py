import numpy as np


class PixelGroup:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)


    def add(self, other):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] += other.matrix[x][y]

    def divide(self, divisor):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] /= divisor

if __name__ == '__main__':
    A = PixelGroup([[3,6],[9,3]])
    A.divide(3)
    print('uwu')