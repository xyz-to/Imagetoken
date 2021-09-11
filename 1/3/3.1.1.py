"""用6x6矩阵表示真实图像的线性空间滤波"""
import numpy as np


def correl2d(image, window):
    """进行线性空间滤波"""
    m = window.shape[0]
    n = window.shape[1]

    # 将矩阵加上mxn的零元素边框
    image1 = np.zeros((image.shape[0] + m - 1, image.shape[1] + n - 1), dtype='uint8')

    # 将矩阵的值输入新矩阵，未被赋值的是矩阵的零边界
    image1[(m - 1) // 2:image.shape[0] + (m - 1) // 2, (n - 1) // 2:image.shape[1] + (n - 1) // 2] = image

    # 进行模板和矩阵元素的乘积和操作, 返回新矩阵
    image2 = np.zeros(image.shape, dtype='uint8')
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # image1的取值范围，因为i,j是取的image的索引值,image1的索引值要多m和n
            v = np.multiply(window, image1[i:i + m, j:j + n])
            image2[i, j] = np.sum(v)
    return image1, image2


image = np.array([[1, 2, 1, 0, 2, 3],
                  [0, 1, 1, 2, 0, 1],
                  [3, 0, 2, 1, 2, 2],
                  [0, 1, 1, 0, 0, 1],
                  [1, 1, 3, 2, 2, 0],
                  [0, 0, 1, 0, 1, 0]])
window = np.array([[1, 0, 0],
                   [0, 0, 0],
                   [0, 0, 2]])

image1, image2 = correl2d(image, window)
print(image1)
print(image2)

