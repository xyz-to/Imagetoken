"""最大值滤波器和最小值滤波器"""
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from skimage import data, util

# scipy包里有多种图像处理方法,有效计算numpy矩阵
img = data.astronaut()[:, :, 0]
# 加入胡椒噪音
pepper_img = util.random_noise(img, mode='pepper', seed=None, clip=True)
# 加入盐粒噪音
salt_img = util.random_noise(img, mode='salt', seed=None, clip=True)

# 进行降噪
max_img = ndimage.maximum_filter(pepper_img, (3, 3))
min_img = ndimage.minimum_filter(salt_img, (3, 3))

# 显示图像
plt.figure()
plt.imshow(img, cmap='gray')
plt.figure()
plt.imshow(pepper_img, cmap='gray')
plt.figure()
plt.imshow(salt_img, cmap='gray')
plt.figure()
plt.imshow(max_img, cmap='gray')
plt.figure()
plt.imshow(min_img, cmap='gray')
plt.show()
