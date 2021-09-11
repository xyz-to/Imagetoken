"""索贝尔算子,3x3模板"""

from skimage import data, filters
from matplotlib import pyplot as plt

img = data.camera()

# sobel算子
img_sobel_h = filters.sobel_h(img)
img_sobel_v = filters.sobel_v(img)
img_sobel = filters.sobel(img)

# 显示图像
plt.figure()
plt.imshow(img_sobel_h, cmap='gray')
plt.figure()
plt.imshow(img_sobel_v, cmap='gray')
plt.figure()
plt.imshow(img_sobel, cmap='gray')
plt.show()


