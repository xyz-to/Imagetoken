"""拉普拉斯边缘检测"""

from skimage import data
from matplotlib import pyplot as plt
from skimage.filters import laplace
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

image = data.camera()
image1 = data.coffee()
laplace_image = laplace(image)
laplace_image1 = laplace(image1)

"""二阶导数为零的点为边缘点,即"""
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
ax[0, 0].imshow(image)
ax[0, 0].set_title('原始图像')
ax[0, 1].imshow(laplace_image, cmap='gray')
ax[0, 1].set_title('边缘图像')
ax[1, 0].imshow(image1)
ax[1, 0].set_title('原始图像')
ax[1, 1].imshow(laplace_image1, cmap='gray')
ax[1, 1].set_title('边缘图像')
for i in ax:
    for j in i:
        j.axis('off')
plt.show()

