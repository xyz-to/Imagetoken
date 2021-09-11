"""盒状滤波"""

import numpy as np
from skimage import data
from matplotlib import pyplot as plt
from scipy import signal


def corrol2d(image, window):
    s = signal.correlate2d(image, window, mode='same', boundary='fill')
    return s.astype(np.uint8)


image = data.camera()
window1 = np.ones((3, 3)) / (3 ** 2)
window2 = np.ones((6, 6)) / (6 ** 2)
window3 = np.ones((9, 9)) / (9 ** 2)

image1 = corrol2d(image, window1)
image2 = corrol2d(image, window2)
image3 = corrol2d(image, window3)

plt.figure()
plt.imshow(image1, cmap='gray')

plt.figure()
plt.imshow(image2, cmap='gray')

plt.figure()
plt.imshow(image3, cmap='gray')

plt.show()
