"""将灰度值转换为RGB值的图像"""
from matplotlib import pyplot as plt
import numpy as np
from skimage import data, color

L = 255


def GetR(gray):
    """转换灰度值的R通道部分"""
    if gray < L / 2:
        return 0
    elif gray > 3 * L / 4:
        return L
    else:
        return 4 * L - 4 * gray


def GetG(gray):
    """转换灰度值的G通道部分"""
    if gray < L / 4:
        return 4 * gray
    elif gray > 3 * L / 4:
        return 4 * L - 4 * gray
    else:
        return L


def GetB(gray):
    """转换灰度值的B通道部分"""
    if gray < L / 4:
        return L
    elif gray > L / 2:
        return 0
    else:
        return 2 * L - 4 * gray


# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 15
plt.rcParams['axes.unicode_minus'] = False

# 设置x , y轴的值
x = [0, 64, 127, 191, 255]
R = []
for i in x:
    R.append(GetR(i))

# 绘制R通道的映射关系
plt.figure()
plt.plot(x, R, 'r--', label='红色变换')
plt.legend(loc='best')

R = []
for i in x:
    R.append(GetB(i))

# 绘制B通道的映射关系
plt.figure()
plt.plot(x, R, 'b--', label='蓝色变换')
plt.legend(loc='best')

R = []
for i in x:
    R.append(GetG(i))

# 绘制R通道的映射关系
plt.figure()
plt.plot(x, R, 'g--', label='绿色变换')
plt.legend(loc='best')

plt.show()

"""将灰度图像转换为彩色图像"""
graying = color.rgb2gray(data.coffee())*255
coloring = np.zeros(data.coffee().shape, dtype='uint8')
for i in range(coloring.shape[0]):
    for j in range(coloring.shape[1]):
        v = graying[i, j]
        r, g, b = GetR(v), GetG(v), GetB(v)
        coloring[i, j, :] = (r, g, b)

# 显示原灰度图像
plt.figure()
plt.axis('off')
plt.imshow(graying, cmap='gray')

# 显示转换的颜色图像
plt.figure()
plt.imshow(coloring)
plt.axis('off')
plt.show()
