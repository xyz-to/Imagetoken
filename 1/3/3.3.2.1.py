"""拉普拉斯算子"""

from matplotlib import pyplot as plt
from skimage import filters, data

img = data.camera()

img_laplace = filters.laplace(img, ksize=3, mask=None)
img_enhance = img + img_laplace

plt.figure()
plt.imshow(img, cmap='gray')
plt.figure()
plt.imshow(img_laplace, cmap='gray')
plt.figure()
plt.imshow(img_enhance, cmap='gray')
plt.show()
