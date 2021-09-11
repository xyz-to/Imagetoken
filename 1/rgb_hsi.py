"""将RGB图像转换为SHI图像"""
from matplotlib import pyplot as plt
import math
import numpy as np
import sys
from skimage import data, io


def rgb_hsi(r1, g1, b1):
    """将RGB元素转换为HSI元素"""
    r2 = r1 / 255
    g2 = g1 / 255
    b2 = b1 / 255
    i1 = (r2 + g2 + b2) / 3
    if (r2 + g2 + b2) == 0:
        s1 = 0
    else:
        s1 = 1 - (3 * min(r2, g2, b2) / (r2 + g2 + b2))
    num = ((r2 - g2) + (r2 - b2)) / 2
    den = ((r2 - g2) * (r2 - g2) + (r2 - b2) * (g2 - b2)) ** 0.5
    if g2 >= b2:
        if den == 0:
            den = sys.float_info.min
        h1 = math.acos(num / den)
    elif g2 < b2:
        if den == 0:
            den = sys.float_info.min
        h1 = (2 * math.pi) - math.acos(num / den)
    return int(h1*10), int(s1 * 100), int(i1 * 255)


image = io.imread(fname='flower.png')
image_hsi = np.zeros(image.shape, dtype='uint8')
# 替换三通道的灰度值
for ii in range(image_hsi.shape[0]):
    for jj in range(image_hsi.shape[1]):
        r, g, b = image[ii, jj, :]
        h, s, i = rgb_hsi(r, g, b)
        image_hsi[ii, jj, :] = (h, s, i)
plt.figure()
plt.axis('off')
# 原图像
plt.imshow(image)
plt.figure()
plt.axis('off')
# R分量图像
plt.imshow(image[:, :, 0], cmap='gray')
plt.figure()
plt.axis('off')
# H分量图像
plt.imshow(image_hsi[:, :, 0], cmap='gray')
plt.figure()
plt.axis('off')
# S分量图像
plt.imshow(image_hsi[:, :, 1], cmap='gray')
plt.figure()
plt.axis('off')
# I分量图像
plt.imshow(image_hsi[:, :, 2], cmap='gray')
plt.show()
