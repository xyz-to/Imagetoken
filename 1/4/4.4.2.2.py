"""Butterworth高通滤波.加上增强"""

import numpy as np
import matplotlib.pyplot as plt
import math
from skimage import data, color


def butterWorthPassFilter(image, d, n):
    """低通滤波处理"""
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    rows = fshift.shape[0]
    cols = fshift.shape[1]
    row = rows / 2  # 中心点
    col = cols / 2
    mask = np.zeros((rows, cols))  # 求滤波模板

    for i in range(rows):
        for j in range(cols):
            if (i - row) ** 2 + (j - col) ** 2 == 0:
                mask[i, j] = 0
            else:
                mask[i, j] = 1 / (1 + d / (math.sqrt((i - row) ** 2 + (j - col) ** 2)) ** (2 * n)) + 1  # 求每个H(u, v)

    fshift = fshift * mask
    f_ishift = np.fft.ifftshift(fshift)  # 转回图像
    img_back = np.abs(np.fft.ifft2(f_ishift))

    return img_back


img = data.coffee()
img = color.rgb2gray(img)

plt.subplot(221)
plt.axis('off')
plt.imshow(img, cmap='gray')
plt.subplot(222)
plt.axis('off')
img_1 = butterWorthPassFilter(img, 100, 1)
plt.imshow(img_1, cmap='gray')
plt.subplot(223)
plt.axis('off')
img_2 = butterWorthPassFilter(img, 30, 1)
plt.imshow(img_2, cmap='gray')
plt.subplot(224)
plt.axis('off')
img_3 = butterWorthPassFilter(img, 30, 5)
plt.imshow(img_3, cmap='gray')
plt.show()
