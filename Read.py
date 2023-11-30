import numpy as np
from matplotlib import pyplot as plt
def Read(file, samples):
    matrix = 28
    with open(file, 'rb') as fid:

        # t1 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
        # t2 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
        # t3 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
    # plt.subplot(131)
    # plt.imshow(t1)
    # plt.show()

    # for _ in range (4):
        img = np.fromfile(fid, dtype=np.uint8, count=samples*matrix*matrix).reshape((samples,matrix,matrix))
    return img



