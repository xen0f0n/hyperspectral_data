import scipy.io as sio
from scipy.misc import imsave
import numpy as np

data = sio.loadmat('/home/xen0f0n/hyperspectral_data_classification/PaviaU.mat')

test_img = np.zeros(shape=(610,340))
for i in range(610):
    for j in range(340):
        # i, j indexes for spatial dimensions, spectral channel 100th
        test_img[i][j] = data['paviaU'][i][j][100]

imsave('test_img.png', test_img)

true_color_img = np.zeros(shape=(610,340, 3))
for i in range(610):
    for j in range(340):
        # i, j indexes for spatial dimensions, spectral channel 100th
        true_color_img[i][j][0] = data['paviaU'][i][j][45] # RED channel
        true_color_img[i][j][1] = data['paviaU'][i][j][27] # GREEN channel
        true_color_img[i][j][2] = data['paviaU'][i][j][11] # BLUE channel

imsave('true_color_img.png', true_color_img)
