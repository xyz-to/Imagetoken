"""空间滤波之罗伯特梯度算子"""
from skimage import data, filters
from matplotlib import pyplot as plt

img = data.camera()

# 罗伯特交叉梯度算子
img_robert_pos = filters.roberts_pos_diag(img)
img_robert_neg = filters.roberts_neg_diag(img)
img_robert = filters.roberts(img)

# 显示图像
plt.figure()
plt.imshow(img_robert_pos, cmap='gray')
plt.figure()
plt.imshow(img_robert_neg, cmap='gray')
plt.figure()
plt.imshow(img_robert, cmap='gray')
plt.show()
