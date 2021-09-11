"""一般颜色直方图"""

from skimage import exposure, data
import matplotlib.pyplot as plt

img = data.coffee()

hist_r = exposure.histogram(img[:, :, 0], nbins=256)
hist_g = exposure.histogram(img[:, :, 1], nbins=256)
hist_b = exposure.histogram(img[:, :, 2], nbins=256)

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.subplot(222)
plt.imshow(hist_r, cmap='gray')
plt.subplot(223)
plt.imshow(hist_g, cmap='gray')
plt.subplot(224)
plt.imshow(hist_b, cmap='gray')
plt.show()
