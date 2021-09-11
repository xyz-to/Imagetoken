"""图像点运算之幂运算"""
from matplotlib import pyplot as plt
from skimage import data, exposure, io

image = data.coffee()
image_1 = exposure.adjust_gamma(image, 0.2)
image_2 = exposure.adjust_gamma(image, 0.7)
image_3 = exposure.adjust_gamma(image, 1.5)
plt.subplot(2, 2, 1)
plt.title('gamma = 0.2')
io.imshow(image_1)
plt.subplot(2, 2, 2)
plt.title('gamma = 0.7')
io.imshow(image_2)
plt.subplot(2, 2, 3)
plt.title('gamma = 1.5')
io.imshow(image_3)
plt.subplot(2, 2, 4)
plt.title('gamma = 1')
io.imshow(image)
plt.show()