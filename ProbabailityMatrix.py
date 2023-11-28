import numpy as np

from PixelGroup import PixelGroup


class ProbabilityMatrix:
    def __init__(self, Pixels, sampleSize):
        self.Pixels = Pixels
        self.sampleSize = sampleSize
        self.SampleGroupsProbabibilities = np.empty_like(object, dtype=PixelGroup, shape=[27, 27])
        self.SampleGroupsProbabibilities.fill(PixelGroup([[1.0, 1.0], [1.0, 1.0]]))
        for x in range(sampleSize):
            self.SumPixel(x)
        self.SampleProbabilities(255 * self.sampleSize + 1)
    def SumPixel(self, sampleNum):
        for x in range(len(self.Pixels[sampleNum]) -1):
            for y in range(len(self.Pixels[sampleNum][x]) - 1):
                self.SampleGroupsValues[x][y].add(self.Pixels[sampleNum][x][y])


    def SampleProbabilities(self, divisor):
        for x in range(len(self.SampleGroupsValues) -1):
            for y in range(len(self.SampleGroupsValues[x]) - 1):
                self.SampleGroupsValues[x][y].divide(divisor)