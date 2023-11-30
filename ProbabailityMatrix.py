import math

import numpy as np

from PixelGroup import PixelGroup


class ProbabilityMatrix:
    def __init__(self, Pixels, sampleSize):
        self.Pixels = Pixels
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

    def SumPixel(self, sampleNum):
        sum = self.SampleGroupsProbabibilities
        for x in range(len(self.SampleGroupsProbabibilities)):
            for y in range(len(self.SampleGroupsProbabibilities[x])):
                sum[x][y].add(self.Pixels[sampleNum][x][y])
        self.SampleGroupsProbabibilities = sum

    def SampleProbabilities(self, divisor):
        for x in range(len(self.SampleGroupsProbabibilities)):
            for y in range(len(self.SampleGroupsProbabibilities[x])):
                self.SampleGroupsProbabibilities[x][y].add(PixelGroup(-math.log(divisor)*np.ones(shape=[2,2])))

    def logPixels(self):
        for x in range(len(self.SampleGroupsProbabibilities)):
            for y in range(len(self.SampleGroupsProbabibilities[x])):
                self.SampleGroupsProbabibilities[x][y].log()

if __name__ == '__main__':
    A = PixelGroup([[255.0, 0.0], [0.0, 0.0]])
    B = PixelGroup([[255.0, 255.0], [255.0, 0.0]])
    Pix = ProbabilityMatrix(np.array([[[A, B], [A, B]], [[A, B], [A, B]], [[A, B], [A, B]]]), 3)
    print('uwu')
