"""边缘检测索贝尔算子"""

from skimage.filters import sobel, sobel_v, sobel_h
import matplotlib.pyplot as plt
import skimage.data as data
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

image = data.camera()
sobel_image = sobel(image)
sobel_v_image = sobel_v(image)
sobel_h_image = sobel_h(image)

# 显示
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 4))
ax[0, 0].imshow(image, cmap='gray')
ax[0, 0].set_title = '原始图像'
ax[0, 1].imshow(sobel_image, cmap='gray')
ax[0, 1].set_title = '边缘图像'
ax[1, 0].imshow(sobel_v_image, cmap='gray')
ax[1, 0].set_title = '垂直边缘图像'
ax[1, 1].imshow(sobel_h_image, cmap='gray')
ax[1, 1].set_title = '水平边缘图像'
for a in ax:
    for b in a:
        b.axis('off')
plt.show()
