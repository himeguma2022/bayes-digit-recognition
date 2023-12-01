import numpy as np

from TestCase import TestCase
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


def ColumnCut(sample):
    out = np.empty_like(object, dtype= np.uint8, shape = [28,28])
    for x in range(len(sample)):
        for y in range(len(sample[x])):
            if y % 29 != 28:
                match sample[x][y]:
                    case 32:
                        out[x][y] = 0
                    case 43:
                        out[x][y] = 128
                    case 35:
                        out[x][y] = 255
    return out


def ReadTest(Images, Labels, Samples):
    matrix = 28
    with open(Labels, 'rb') as fid:
        TestLabels = np.fromfile(fid, dtype=np.uint8, count=Samples * 2)
    with open(Images, 'rb') as fid:
        ImageData = np.fromfile(fid, dtype=np.uint8, count=Samples * matrix * (matrix+1)).reshape((Samples,matrix,matrix + 1))

    for x in range(len(TestLabels)):
        TestLabels[x] -= 48
    TestAns = TestLabels[TestLabels != 218]
    ImageDataProcessed = []

    for sample in range(len(ImageData)):
        ImageDataProcessed.append(TestCase(ColumnCut(ImageData[sample]), TestAns[sample]))
    return ImageDataProcessed


def NaieveBayes(image, Probabilites):
    imageGroup = PixelToGroups(image)
    for x in range(len(imageGroup)):
        for y in range(len(imageGroup[x])):
            imageGroup[x][y].log()
    Scores = np.array([0.0]*10)
    for digit in range(len(Probabilites)):
        for x in range(len(imageGroup)):
            for y in range(len(imageGroup[x])):
                pixGroupEval = PixelGroup([[0,0],[0,0]])
                pixGroupEval.add(imageGroup[x][y])
                pixGroupEval.add(Probabilites[digit].SampleGroupsProbabibilities[x][y])
                Scores[digit] += pixGroupEval.sumElements()
    for x in range(len(Scores)):
        print(f'{x}->{Scores[x]}')
    Max = Scores.max()
    print(f'Guesssed {np.where(Scores == Max)}')
    return np.where(Scores == Max)




def ClassifyCorrect(test, ProbClassProbabilites):
    print(test.answer)
    return test.answer == NaieveBayes(test.image,ProbClassProbabilites)


if __name__ == '__main__':
    ProbClasses = ["data0", "data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9"]
    ProbClassProbabilites = []
    for x in ProbClasses:
        ProbClassProbabilites.append(ProbMatrixGenerate(x, 10))
    TestImages = ReadTest("testimages", "testlabels", 1)
    Result = []
    for test in TestImages:
        Result.append(ClassifyCorrect(test, ProbClassProbabilites))
    print('yolo')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
