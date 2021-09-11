"""rgb图像分割"""

from skimage import io
from matplotlib import pyplot as plt
import numpy as np
import math

image = io.imread('flower.png')
r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]

# 显示RGB各分量的图像
plt.subplot(221)
plt.title('r')
plt.imshow(r)
plt.subplot(222)
plt.title('g')
plt.imshow(g)
plt.subplot(223)
plt.title('b')
plt.imshow(b)
plt.show()

# 选择样本区域
r1 = r[133:250, 177:330]

# 样本的平均值
r1_u = np.mean(r1)

# 计算样本的标准差
r1_b = 0.0
for i in range(r1.shape[0]):
    for j in range(r1.shape[1]):
        r1_b = r1_b + (r1[i, j] - r1_u) * (r1[i, j] - r1_u)
r1_d = math.sqrt(r1_b / r1.shape[0] / r1.shape[1])

# 找到符合标准差的点
r2 = np.zeros(r.shape, dtype='uint8')
for i in range(r2.shape[0]):
    for j in range(r2.shape[1]):
        if (r1_u - 1.50 * r1_d) <= r[i, j] <= (r1_u + 1.25 * r1_d):
            r2[i, j] = 1

# 根据找到的点分割
image2 = np.zeros(image.shape, dtype='uint8')
for i in range(image2.shape[0]):
    for j in range(image2.shape[1]):
        if r2[i, j] == 1:
            image2[i, j, :] = image[i, j, :]

plt.figure()
plt.axis('off')
plt.imshow(image2)
plt.show()
