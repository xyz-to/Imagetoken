"""反锐化掩蔽"""

from matplotlib import pyplot as plt
from scipy import signal
from skimage import data
import numpy as np

img = data.camera()


def correl2d(image, window):
    s = signal.correlate2d(image, window, mode='same', boundary='fill')
    return s


window_1 = np.ones((3, 3)) / 9
img_blur = correl2d(img, window_1)
img_edge = img - img_blur
img_enhance = img_edge + img

plt.figure()
plt.imshow(img, cmap='gray')
plt.figure()
plt.imshow(img_blur, cmap='gray')
plt.figure()
plt.imshow(img_edge, cmap='gray')
plt.figure()
plt.imshow(img_enhance, cmap='gray')
plt.show()

