import math

import numpy as np

from PixelGroup import PixelGroup


def MatrixCopy(SampleGroupsProbabibilities):
    dims = len(SampleGroupsProbabibilities)
    out = np.empty_like(object, shape=[dims, dims], dtype=PixelGroup)
    for x in range(len(SampleGroupsProbabibilities)):
        for y in range(len(SampleGroupsProbabibilities[x])):
            out[x][y] = SampleGroupsProbabibilities[x][y].__copy__()
    return out


class ProbabilityMatrix:
    def __init__(self, Pixels, sampleSize):
        self.Pixels = Pixels
        self.logged = False
        self.sampleSize = sampleSize
        self.imageSize = len(Pixels[0])
        self.SampleGroupsProbabibilities = np.empty_like(object, shape=[self.imageSize, self.imageSize], dtype=PixelGroup)
        for x in range(len(self.SampleGroupsProbabibilities)):
            for y in range(len(self.SampleGroupsProbabibilities[x])):
                self.SampleGroupsProbabibilities[x][y] = PixelGroup([[1,1],[1,1]])
        for x in range(sampleSize):
            self.SumPixel(x)
        self.logPixels()
        self.SampleProbabilities(255 * self.sampleSize + 1)
        self.compProbs = self.compProbabilities()

    def SumPixel(self, sampleNum):
        sum = self.SampleGroupsProbabibilities
        for x in range(len(self.SampleGroupsProbabibilities)):
            for y in range(len(self.SampleGroupsProbabibilities[x])):
                sum[x][y].add(self.Pixels[sampleNum][x][y])
        self.SampleGroupsProbabibilities = sum

    def SampleProbabilities(self, divisor):
        if self.logged != True:
            self.logPixels()
        for x in range(len(self.SampleGroupsProbabibilities)):
            for y in range(len(self.SampleGroupsProbabibilities[x])):
                self.SampleGroupsProbabibilities[x][y].add(PixelGroup(-math.log(divisor)*np.ones(shape=[2,2])))

    def logPixels(self):
        self.logged = True
        for x in range(len(self.SampleGroupsProbabibilities)):
            for y in range(len(self.SampleGroupsProbabibilities[x])):
                self.SampleGroupsProbabibilities[x][y].log()

    def inlogPixels(self):
        self.logged = False
        for x in range(len(self.SampleGroupsProbabibilities)):
            for y in range(len(self.SampleGroupsProbabibilities[x])):
                self.SampleGroupsProbabibilities[x][y].inlog()

    def compProbabilities(self):
        if self.logged:
            self.inlogPixels()
        negProb = MatrixCopy(self.SampleGroupsProbabibilities)
        out = np.empty_like(object, shape=[self.imageSize, self.imageSize], dtype=PixelGroup)
        for x in range(len(out)):
            for y in range(len(out[x])):
                out[x][y] = PixelGroup([[1,1],[1,1]])
                negProb[x][y].divide(-1)
                out[x][y].add(negProb[x][y])
        return out

if __name__ == '__main__':
    A = PixelGroup([[255.0, 0.0], [0.0, 0.0]])
    B = PixelGroup([[255.0, 128.0], [128.0, 0.0]])
    Pix = ProbabilityMatrix(np.array([[[A, B], [A, B]], [[A, B], [A, B]], [[A, B], [A, B]]]), 3)
    CompPix = Pix.compProbabilities()
    print('uwu')
