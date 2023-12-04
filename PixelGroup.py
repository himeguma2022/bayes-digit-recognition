import math

import numpy as np


class PixelGroup:
    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype=float)
        self.logged = False

    def __copy__(self):
        outMatrix = np.array(self.matrix)
        copy = PixelGroup(outMatrix)
        if self.logged:
            copy.logged = True
        return copy

    def add(self, other):
        sum = np.add(self.matrix, other.matrix)
        self.matrix = sum

    def divide(self, divisor):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] /= divisor

    def log(self):
        self.logged = True
        if 0 in self.matrix:
            self.add(PixelGroup(0.01*np.ones(shape=self.matrix.shape)))
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = math.log(self.matrix[x][y])

    def inlog(self):
        self.logged = False
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = math.pow(math.e,self.matrix[x][y])

    def flip(self):
        if self.logged:
            self.inlog()
            return self.flip()
        W=PixelGroup([[255,255],[255,255]])
        self.matrix = self.matrix*-1
        W.add(self)
        W.log()
        return W

    def mean(self):
        if self.logged:
            self.inlog()
            return self.mean()
        summ = self.matrix.sum()
        return summ/(len(self.matrix)*len(self.matrix[0]))

    def sumElements(self):
        if self.logged:
            self.inlog()
            return self.sumElements()
        return self.matrix.sum()

if __name__ == '__main__':
    A = PixelGroup([[3,6],[9,3]])
    A.divide(3)
    B = PixelGroup([[3,2],[1,3]])
    C = PixelGroup([[1,1],[1,1]])
    A.add(B)
    D = A.__copy__()
    A.add(C)
    A.add(C)
    print(A.mean())
    print(B.mean())
    print('uwu')