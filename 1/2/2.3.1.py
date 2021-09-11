"""二值饱和度分割"""
from matplotlib import pyplot as plt
from skimage import io
import numpy as np
import sys
import math

image = image = io.imread(fname='flower.png')
image_hsi = np.zeros(image.shape, dtype='uint8')


def rgb_hsi(r1, g1, b1):
    """将RGB元素转换为HSI元素"""
    r2 = r1 / 255
    g2 = g1 / 255
    b2 = b1 / 255
    i1 = (r2 + g2 + b2) / 3
    if (r2 + g2 + b2) == 0:
        s1 = 0
    else:
        s1 = 1 - (3 * min(r2, g2, b2) / (r2 + g2 + b2))
    num = ((r2 - g2) + (r2 - b2)) / 2
    den = ((r2 - g2) * (r2 - g2) + (r2 - b2) * (g2 - b2)) ** 0.5
    if g2 >= b2:
        if den == 0:
            den = sys.float_info.min
        h1 = math.acos(num / den)
    elif g2 < b2:
        if den == 0:
            den = sys.float_info.min
        h1 = (2 * math.pi) - math.acos(num / den)
    return int(h1*10), int(s1 * 100), int(i1 * 255)


# 将图像从RGB转换为HSI
for ii in range(image.shape[0]):
    for jj in range(image.shape[1]):
        r, g, b = image[ii, jj, :]
        h, s, i = rgb_hsi(r, g, b)
        image_hsi[ii, jj, :] = (h, s, i)

# 读取HSI的值
H = image_hsi[:, :, 0]
S = image_hsi[:, :, 1]
I1 = image_hsi[:, :, 2]

# 生成二值饱和度模板
S_template = np.zeros(S.shape, dtype='uint8')
for i in range(S.shape[0]):
    for j in range(S.shape[1]):
        if S[i, j] > 0.8 * S.max():
            S_template[i, j] = 1
print('模板生成')
# 将色调图像与模板相乘得到分割结果
F = np.zeros(H.shape, dtype='uint8')
for i in range(F.shape[0]):
    for j in range(F.shape[1]):
        F[i, j] = S_template[i, j] * H[i, j]
print('分割完成')

# 显示分割后的图片
plt.figure()
plt.axis('off')
plt.imshow(F, cmap='gray')
plt.show()
