from PixelGroup import PixelGroup
from Read import Read


def GroupRow(row, lastRow):
    GroupRow = []
    lastCol = row[0]
    colCount = 1
    for col in row:
        if col == row[0]:
            pass
        if colCount == 28:
            break
        GroupRow.append(PixelGroup([[lastRow[colCount - 1],lastRow[colCount]],[row[colCount - 1],row[colCount]]]))
        colCount+= 1
    return GroupRow

def PixelToGroups(matrix):
    GroupMatrix = []
    lastRow = DataMatrix[0][0]
    for row in DataMatrix[0]:
        if (row == DataMatrix[0][0]).all:
            pass
        GroupMatrix.append(GroupRow(row, lastRow))
        lastRow = row
    return GroupMatrix

if __name__ == '__main__':
    DataMatrix = Read("data0")
    SampleGroups = []
    for x in range(len(DataMatrix)):
        SampleGroups.append(PixelToGroups(DataMatrix[x]))

    print(DataMatrix[0][7][15])
    print(DataMatrix[0][7][14])
    print('yolo')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
