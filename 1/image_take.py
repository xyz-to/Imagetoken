"""针对图像基本属性的操作"""
import numpy as np
from skimage import data
from matplotlib import pyplot as plt
from skimage import io


def change_alpha(im, a):
    """改变图像的对比度"""
    image = np.zeros(shape=im.shape, dtype='int32')
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                v = im[i, j, k] * a
                if v >= 255:
                    image[i, j, k] = 255
                elif v <= 0:
                    image[i, j, k] = 0
                else:
                    image[i, j, k] = v
    return image


"""三通道操作"""
image_1 = data.coffee()
image_r = image_1[:, :, 0]
image_g = image_1[:, :, 1]
image_b = image_1[:, :, 2]
plt.subplot(2, 2, 1)
plt.imshow(image_r)
plt.subplot(2, 2, 2)
plt.imshow(image_g)
plt.subplot(2, 2, 3)
plt.imshow(image_b)
plt.subplot(2, 2, 4)
plt.imshow(image_1)
plt.show()

