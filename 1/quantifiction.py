"""图像量化，量化到只有2灰度级别"""
from skimage1 import data

from matplotlib import pyplot as plt

image = data.cat()
ratio = 128  # 量化比率
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        for k in range(image.shape[2]):
            image[i, j, k] = int(image[i, j, k]/ratio)*ratio
plt.imshow(image)
plt.show()
