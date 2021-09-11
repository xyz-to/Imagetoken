"""彩色图像的灰度化"""
import numpy as np
from matplotlib import pyplot as plt
from skimage import data

image = data.coffee()
# 最大灰度化
max_gray = np.zeros(image.shape[0:2], dtype='uint8')
# 平均灰度化
ave_gray = np.zeros(image.shape[0:2], dtype='uint8')
# 加权灰度化
weight_gray = np.zeros(image.shape[0:2], dtype='uint8')

# 灰度化处理
for ii in range(image.shape[0]):
    for jj in range(image.shape[1]):
        r, g, b = image[ii, jj, :]
        max_gray[ii, jj] = max(r, g, b)
        ave_gray[ii, jj] = r / 3 + g / 3 + b / 3
        weight_gray[ii, jj] = 0.3 * r + 0.59 * g + 0.11 * b

# 显示结果
plt.figure()
plt.axis('off')
plt.imshow(image)

plt.figure()
plt.axis('off')
plt.imshow(max_gray, cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(ave_gray, cmap='gray')

plt.figure()
plt.axis('off')
plt.imshow(weight_gray, cmap='gray')

plt.show()
