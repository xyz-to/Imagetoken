"""使用高斯平滑滤波器对图像处理"""

import numpy as np
from skimage import data
from matplotlib import pyplot as plt
import math
from scipy import signal


def guass(i, j, sigma):
    """计算每个高斯点的值"""
    return 1 / (2 * math.pi * sigma ** 2) * math.exp(-(i ** 2 + j ** 2) / (2 * sigma ** 2))


def correl2d(imagec, window):
    """滤波变化，mode表示输出尺寸等于输出尺寸"""
    s = signal.correlate2d(imagec, window, boundary='fill', mode='same')
    return s.astype(np.uint8)


def guass_window(radius, sigma):
    """返回指定的高斯滤波模板"""
    window = np.zeros((radius, radius))
    rol = radius // 2
    for i in range(-rol, rol + 1):
        for j in range(-rol, rol + 1):
            window[i + rol][j + rol] = guass(i, j, sigma)
    print(window)
    return window / np.sum(window)


image = data.camera()
window_1 = guass_window(3, 1.0)
window_2 = guass_window(5, 1.0)
window_3 = guass_window(9, 1.0)

image_1 = correl2d(image, window_1)
image_2 = correl2d(image, window_2)
image_3 = correl2d(image, window_3)

plt.figure()
plt.imshow(image_1, cmap='gray')
plt.figure()
plt.imshow(image_2, cmap='gray')
plt.figure()
plt.imshow(image_3, cmap='gray')

plt.show()
