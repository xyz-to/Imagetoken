"""理想高通滤波处理器"""

import matplotlib.pyplot as plt
import numpy as np
from skimage import data, color
from pylab import mpl
import math

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

img = data.coffee()
new_img = color.rgb2gray(img)
D = 10

# 傅里叶变换
f1 = np.fft.fft2(new_img)
f1_shift = np.fft.fftshift(f1)

# 低通滤波，欧式距离小于D的为1，其他为0
rows = f1_shift.shape[0]
cols = f1_shift.shape[1]
row = rows/2
col = cols/2
mask = np.ones((rows, cols), np.uint8)
for i in range(rows):
    for j in range(cols):
        if math.sqrt((i - row) ** 2 + (j - col) ** 2) <= D:
            mask[i, j] = 0
f1_shift = f1_shift * mask

# 傅里叶逆变换
f_ishift = np.fft.ifftshift(f1_shift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# 图像显示
plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('原始图像')

plt.subplot(122)
plt.imshow(img_back, 'gray')
plt.title('滤波图像')

plt.show()