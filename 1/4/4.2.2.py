"""使用两次一维傅里叶变换代替一维傅里叶变换"""

from skimage import data, color
import numpy as np
import matplotlib.pyplot as plt
img = data.coffee()
img_1 = color.rgb2gray(img)
m, n = img_1.shape
fx = img_1
for x in range(n):
    fx[:, x] = np.fft.fft(img_1[:, x])
for y in range(m):
    fx[y, :] = np.fft.fft(img_1[y, :])
fshift = np.fft.fftshift(fx)
img_f = np.log(np.abs(fshift))
plt.subplot(121)
plt.imshow(img)
plt.title('原始图像')
plt.subplot(122)
plt.imshow(img_f, 'gray')
plt.title('傅里叶图像')
plt.show()

