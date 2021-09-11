"""图像直方图"""
from skimage import data, exposure, io
from matplotlib import pyplot as plt


image = data.coffee()
hist_r = exposure.histogram(image[:, :, 0], nbins=256)
hist_g = exposure.histogram(image[:, :, 1], nbins=256)
hist_b = exposure.histogram(image[:, :, 2], nbins=256)
plt.figure('hist', figsize=(8, 8))
plt.subplot(221)
plt.title('')
io.imshow(image)
plt.subplot(222)
plt.title('r')
plt.hist(hist_r, edgecolor='None', facecolor='red')
plt.subplot(223)
plt.title('g')
plt.hist(hist_g)
plt.subplot(224)
plt.title('b')
plt.hist(hist_b)
plt.show()