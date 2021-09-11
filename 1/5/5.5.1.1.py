"""边角检测"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.data as data


def susan_corner_detection(img):
    # 将数据类型改为浮点型
    img = img.astype(np.float64)
    g = 10  # 阈值
    output = np.zeros(img.shape)  # 将要输出的数组
    # 从三开始，因为模板是7元素，不能溢出
    for i in range(3, img.shape[0]):
        for j in range(3, img.shape[1]):
            r0 = img[i, j]
            r = img[i - 3:i + 4, j - 3:j + 4]
            nr = np.sum(np.exp(-((r0 - r) / 6) ** 6))
            if nr < g:
                output[i, j] = g-nr

    # 非最大抑制
    for i in range(1, img.shape[0]):
        for j in range(1, img.shape[1]):
            arr = img[i-1:i+1, j-1:j+1]
            if img[i, j] < np.max(arr):
                img[i, j] = 0

    return output


image = data.camera()
image_out = susan_corner_detection(image)
plt.imshow(image_out, cmap='gray')
plt.show()

