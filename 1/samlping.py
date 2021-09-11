"""图像采样，平均值"""
from skimage1 import data

import numpy as np
from matplotlib import pyplot as plt

image = data.cat()  # 获取图像
print(image.shape)
ratio = 10  # 设置采样比率
image1 = np.zeros((int(image.shape[0] / ratio),
                   int(image.shape[1] / ratio),
                   image.shape[2]), dtype='int32')
for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in range(image1.shape[2]):
            delta = image[i * ratio:(i + 1) * ratio, j * ratio:(j + 1) * ratio, k]
            image1[i, j, k] = np.mean(delta)
plt.imshow(image1)
plt.show()
plt.imshow(image)
plt.show()
