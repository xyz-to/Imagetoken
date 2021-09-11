"""基于二值模式的图像纹理分类"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.feature import local_binary_pattern
from skimage.color import label2rgb
from skimage.transform import rotate


METHOD = 'uniform'
plt.rcParams['font.size'] = 9


def plot_circle(ax, center, radius, color):
    """画圆圈方法"""
    circle = plt.Circle(center, radius, facecolor=color, edgecolor='0.5')
    """将圆圈加入到图片对象中"""
    ax.add_patch(circle)


def plot_lbp_model(ax, binary_values):
    """画出LBP的基础模型"""
    theta = np.deg2rad(45)
    R = 1
    r = 0.15
    w = 1.5
    # 画出中心圆
    plot_circle(ax, (0, 0), radius=r, color='0.5')
    for i, facecolor in enumerate(binary_values):
        x = R * np.cos(theta * i)
        y = R * np.sin(theta * i)
        plot_circle(ax, (x, y), radius=r, color=str(facecolor))
    # 画出网格
    for x in np.linspace(-w, w, 4):  # 返回指定区间内的4个间距的数字序列
        # 在坐标为x,x的点上画一道横线和竖线
        ax.axvline(x, color='gray')
        ax.axhline(x, color='gray')
    # 画出边界
    size = w + 0.2
    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)


# LBP算子分类,即滤波之后对应元素是边缘，平滑，角，还是变化的
fig, axes = plt.subplots(ncols=5, figsize=(7, 2))
titles = ['flat', 'flat', 'edge', 'corner', 'non-uniform']
binary_patterns = [np.zeros(8), np.ones(8),
                   np.hstack([np.ones(4), np.zeros(4)]),
                   np.hstack([np.zeros(3), np.ones(5)]),
                   [1, 0, 0, 1, 1, 1, 0, 0]]
for ax, values, name in zip(axes, binary_patterns, titles):
    plot_lbp_model(ax, values)
    ax.set_title(name)

plt.show()

# 二值模式特征提取


