"""混合空间增强"""
import numpy as np
from matplotlib import pyplot as plt
from skimage import io, filters
from scipy import signal


def correl2d(image, window):
    s = signal.correlate2d(image, window, mode='same', boundary='fill')
    return s


img = io.imread('bone.png', as_gray='True')
# 二阶微分算子，增强图像纹理
img_laplace = filters.laplace(img, ksize=3, mask=None)
img_laplace_enhance = img + img_laplace
# 一阶微分算子，增强图像边缘
img_sobel = filters.sobel(img, mask=None)
# 索贝尔的锐化处理使用反锐化掩蔽
window_sobel = np.ones((5, 5)) / 25
img_sobel_mean = correl2d(img, window_sobel)
# 这里不是减法而是乘法
img_mask = img_sobel_mean * img_laplace_enhance
img_sharp_enhance = img_mask + img

# 幂次处理
img_enhance = img_sharp_enhance ** 0.2

# 显示图像
imgList = [img, img_laplace, img_laplace_enhance, img_sobel, img_sobel_mean, img_mask, img_sharp_enhance, img_enhance]
for i in imgList:
    plt.figure()
    plt.axis('off')
    plt.imshow(i)
plt.show()
