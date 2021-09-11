"""灰度图像的强度分层"""
from skimage import data, color
from matplotlib import pyplot as plt
import numpy as np

image = data.coffee()
# 将图像转换为灰度图像
graying = color.rgb2gray(image)*255
plt.figure()
plt.axis('off')
plt.imshow(graying, cmap='gray')
labels = np.zeros(graying.shape)
for i in range(labels.shape[0]):
    for j in range(labels.shape[1]):
        if graying[i, j] < 0.4:
            labels[i, j] = 0
        elif graying[i, j] < 0.8:
            labels[i, j] = 1
        else:
            labels[i, j] = 2
psding = color.label2rgb(labels)
plt.figure()
plt.axis('off')
plt.imshow(psding)
plt.show()
