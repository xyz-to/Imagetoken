"""LoG算子"""

from skimage import data
from matplotlib import pyplot as plt
from skimage.filters import laplace, gaussian
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

# 先平滑再边缘检测
image = data.camera()
image_gaussian = gaussian(image)
image_laplace = laplace(image)
image_log = laplace(image_gaussian)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
ax[0, 0].imshow(image, cmap='gray')
ax[0, 0].set_title("原始图像")
ax[0, 1].imshow(image_laplace, cmap='gray')
ax[0, 1].set_title("laplace边缘图像")
ax[1, 0].imshow(image_gaussian, cmap='gray')
ax[1, 0].set_title("平滑图像")
ax[1, 1].imshow(image_log, cmap='gray')
ax[1, 1].set_title("log边缘图像")
plt.show()
