"""傅里叶描述符"""

import numpy as np
from matplotlib import pyplot as plt
from skimage import measure

# 构建测试数据
x, y = np.ogrid[-np.pi:np.pi: 100j, -np.pi:np.pi: 100j]
r = np.sin(np.exp(np.sin(x) ** 3 + np.cos(y) ** 3))

# 找出轮廓边界
contours = measure.find_contours(r, 0.8)

# 显示边界
fig, ax = plt.subplots()
ax.imshow(r, cmap='gray')
for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax.set_xticks([])

ax.set_yticks([])
plt.show()

# 傅里叶描述符
coutour_complex = np.empty(contour.shape[:-1], dtype=complex)
coutour_complex.real = contour[:, 0]
coutour_complex.imag = contour[:, 1]
result = np.fft.fft(coutour_complex)
print(result.shape)
