"""局部二值模式"""

import matplotlib.pyplot as plt
import skimage.data as data
import skimage.feature as feature

image = data.coffee()
for channel in range(3):
    image[:, :, channel] = feature.local_binary_pattern(image[:, :, channel], 8, 1.0, method='var')

plt.imshow(image)
plt.show()
