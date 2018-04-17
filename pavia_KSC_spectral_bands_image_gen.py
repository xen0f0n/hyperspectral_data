import scipy.io as sio
import numpy as np
import imageio
from matplotlib import pyplot as plt
import os
# from scipy.misc import imsave

dir_path = os.getcwd()

# Loads PaviaU dataset
# PaviaU.mat loads as a dict
# The array is under the dict's 'paviaU' key
data_pavia = sio.loadmat(dir_path + '/Datasets/PaviaU.mat')

# Initialize a numpy array (2d - only one spectral band)
PAVIA_one_band_img = np.zeros(shape=(610, 340))
for i in range(610):
    for j in range(340):
        # i, j indexes for spatial dimensions, spectral channel 100th
        PAVIA_one_band_img[i][j] = data_pavia['paviaU'][i][j][100]

# imsave('true_color_img.png', true_color_img)
# scipy.misc.imsave is deprecated
imageio.imsave(dir_path + '/Generated_Images/PAVIA_one_band_img.png', PAVIA_one_band_img)


# Initialize a numpy array (3d - it's a true colour image - 3 spectral bands)
PAVIA_true_color_img = np.zeros(shape=(610, 340, 3))
for i in range(610):
    for j in range(340):
        # i, j indexes for spatial dimensions, spectral channel 100th
        PAVIA_true_color_img[i][j][0] = data_pavia['paviaU'][i][j][45]  # RED channel
        PAVIA_true_color_img[i][j][1] = data_pavia['paviaU'][i][j][27]  # GREEN channel
        PAVIA_true_color_img[i][j][2] = data_pavia['paviaU'][i][j][11]  # BLUE channel


imageio.imsave(dir_path + '/Generated_Images/PAVIA_true_color_img.png', PAVIA_true_color_img)


data_gt_pavia = sio.loadmat(dir_path + '/Datasets/PaviaU_gt.mat')

# data_gt_pavia['paviaU_gt'] is a 2d array (no depth)
PAVIA_gt_img = np.zeros(shape=(610, 340))
for i in range(610):
    for j in range(340):
        PAVIA_gt_img[i][j] = data_gt_pavia['paviaU_gt'][i][j]

imageio.imsave(dir_path + '/Generated_Images/PAVIA_gt_img.png', PAVIA_gt_img)


data_KSC = sio.loadmat(dir_path + '/Datasets/KSC.mat')

KSC_false__color_img = np.zeros(shape=(512, 614, 3))
for i in range(512):
    for j in range(614):
        # i, j indexes for spatial dimensions, 3 spectral channels
        KSC_false__color_img[i][j][0] = data_KSC['KSC'][i][j][58]  # RED channel
        KSC_false__color_img[i][j][1] = data_KSC['KSC'][i][j][26]  # GREEN channel
        KSC_false__color_img[i][j][2] = data_KSC['KSC'][i][j][16]  # BLUE channel

imageio.imsave(dir_path + '/Generated_Images/KSC_false__color_img.png', KSC_false__color_img)
# print(data_KSC['KSC'].shape)


KSC_true__color_img = np.zeros(shape=(512, 614, 3))
for i in range(512):
    for j in range(614):
        KSC_true__color_img[i][j][0] = data_KSC['KSC'][i][j][31]
        KSC_true__color_img[i][j][1] = data_KSC['KSC'][i][j][16]
        KSC_true__color_img[i][j][2] = data_KSC['KSC'][i][j][6]

imageio.imsave(dir_path + '/Generated_Images/KSC_true__color_img.png', KSC_true__color_img)


KSC_one_band_img = np.zeros(shape=(512, 614))
for i in range(512):
    for j in range(614):
        # i, j indexes for spatial dimensions, spectral channel 58th
        KSC_one_band_img[i][j] = data_KSC['KSC'][i][j][58]  # RED channel

imageio.imsave(dir_path + '/Generated_Images/KSC_one_band_img.png', KSC_one_band_img)


data_gt_KSC = sio.loadmat(dir_path + '/Datasets/KSC_gt.mat')
# print(data_gt_KSC['KSC_gt'].shape)

KSC_gt_img = np.zeros(shape=(512, 614))
for i in range(512):
    for j in range(614):
        KSC_gt_img[i][j] = data_gt_KSC['KSC_gt'][i][j]

imageio.imsave(dir_path + '/Generated_Images/KSC_gt_img.png', KSC_gt_img)

# To only view the results
# plt.subplot(121)
# plt.imshow(data_gt_KSC_img)
# plt.subplot(122)
# plt.imshow(PAVIA_gt_img)
# plt.show()

# To view and save them
fig = plt.figure()
sub1 = fig.add_subplot(1, 2, 1)
sub1.imshow(KSC_gt_img)
sub2 = fig.add_subplot(1, 2, 2)
sub2.imshow(PAVIA_gt_img)
plt.show()
fig.savefig(dir_path + '/Generated_Images/gt_cmaps.png')
