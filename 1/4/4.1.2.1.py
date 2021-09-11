"""二位傅里叶变换"""

import matplotlib.pyplot as plt
import numpy as np
import skimage.data as data
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

img = data.camera()
# 快速傅里叶变换
f = np.fft.fft2(img)
# 将直流分量移到频谱中央
fshit = np.fft.fftshift(f)
fimg = np.log(np.abs(fshit))
plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('原始图像')
plt.subplot(122)
plt.imshow(fimg, 'gray')
plt.title('原始图像')
plt.show()

