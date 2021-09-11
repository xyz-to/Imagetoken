"""边缘检测罗伯特算子"""

from skimage.filters import roberts
import matplotlib.pyplot as plt
import skimage.data as data
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
image = data.camera()
roberts_image = roberts(image)

# 显示
fig, ax = plt.subplots(ncols=2, figsize=(8, 2))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('原始图像')
ax[1].imshow(roberts_image, cmap='gray')
ax[1].set_title('边缘图像')
for a in ax:
    a.axis('off')
plt.show()
