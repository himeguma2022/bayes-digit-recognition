import numpy as np
from matplotlib import pyplot as plt

matrix = 28 
with open('data2', 'rb') as fid: 

    # t1 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
    # t2 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
    # t3 = np.fromfile(fid, dtype=np.uint8, count=28*28).reshape((28, 28))
# plt.subplot(131)
# plt.imshow(t1)
# plt.show()

    # for _ in range (4): 
    for _ in range(1): 
        img = np.fromfile(fid, dtype=np.uint8, count=matrix*matrix).reshape((matrix,matrix))
        plt.imshow(img)
        plt.show()
        print(img)


