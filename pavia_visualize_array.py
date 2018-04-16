import scipy.io as sio
from scipy.misc import imsave
import numpy as np

mat = sio.loadmat('/home/xen0f0n/Downloads/PaviaU.mat')

a = np.zeros(shape=(610,340))
for i in range(610):
    for j in range(340):
        # i, j indexes for spatial dimensions, spectral channel 100th
        a[i][j] = mat['paviaU'][i][j][100]

imsave('test.png', a)
