import numpy as np

from PixelGroup import PixelGroup
from Read import Read
from ProbabailityMatrix import ProbabilityMatrix


def GroupRow(row, lastRow):
    GroupRow = np.empty_like(object, dtype=PixelGroup, shape = 27)
    for x in range(1,len(row),1):
        GroupRow[x-1]=PixelGroup([[lastRow[x - 1],lastRow[x]],[row[x - 1],row[x]]])
    return GroupRow

def PixelToGroups(matrix):
    GroupMatrix = np.empty_like(object, dtype=PixelGroup, shape=[27,27])
    for row in range(1,len(matrix),1):
        GroupMatrix[row - 1] = (GroupRow(matrix[row],matrix[row - 1]))
    return GroupMatrix

def MapDigit(ProbMatrix):
    Map = np.zeros(shape=[27,27])
    for x in range(len(Map)):
        for y in range(len(Map[x])):
            Map[x][y] = ProbMatrix.SampleGroupsProbabibilities[x][y].mean()
    return Map
def ProbMatrixGenerate(digit, samples):
    DataMatrix = Read(digit, samples)
    SampleGroups = np.empty_like(object, dtype=PixelGroup, shape=[samples, 27, 27])
    for x in range(len(DataMatrix)):
        SampleGroups[x] = PixelToGroups(DataMatrix[x])
    return ProbabilityMatrix(SampleGroups, samples)



if __name__ == '__main__':
    ProbClasses = ["data0", "data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9"]
    ProbClassProbabilites = []
    for x in ProbClasses:
        ProbClassProbabilites.append(ProbMatrixGenerate(x, 10))
    print('yolo')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
