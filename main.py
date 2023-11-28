import numpy as np

from PixelGroup import PixelGroup
from Read import Read


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






if __name__ == '__main__':
    DataMatrix = Read("data0")
    SampleGroups = np.empty_like(object, dtype=PixelGroup, shape=[1000, 27, 27])
    for x in range(len(DataMatrix)):
        SampleGroups[x] = PixelToGroups(DataMatrix[x])
    Probs = ProbabailityMatrix(SampleGroups,1000)

    print(DataMatrix[0][7][15])
    print(DataMatrix[0][7][14])
    print('yolo')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
