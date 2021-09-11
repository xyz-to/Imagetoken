"""中值滤波器降噪"""
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from skimage import data, util

img = data.astronaut()
noise_img = np.zeros(img.shape)
new_img = np.zeros(img.shape)
for i in range(new_img.shape[2]):
    graying = img[:, :, i]
    # 对原始图像添加椒盐噪声
    noise_img[:, :, i] = util.random_noise(graying, mode='s&p', seed=None, clip=True)
    # 中值滤波
    new_img[:, :, i] = ndimage.median_filter(noise_img[:, :, i], (3, 3))

# 显示图像
plt.figure()
plt.imshow(img)
plt.figure()
plt.imshow(noise_img)
plt.figure()
plt.imshow(new_img)
plt.show()


