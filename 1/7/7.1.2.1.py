"""傅里叶变换"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

# x坐标的等差数列
t = np.linspace(0, 1, 400, endpoint=False)
cond = [t < 0.25, (t >= 0.25) & (t < 0.5), t >= 0.5]

# lambda函数,冒号左边参数,冒号右边操作
f1 = lambda t: np.cos(2 * np.pi * 10 * t)
f2 = lambda t: np.cos(2 * np.pi * 50 * t)
f3 = lambda t: np.cos(2 * np.pi * 100 * t)

# y坐标,piecewise操作函数
y1 = np.piecewise(t, cond, [f1, f2, f3])
y2 = np.piecewise(t, cond, [f2, f1, f3])

Y1 = abs(fft(y1))
Y2 = abs(fft(y2))

# 显示
plt.figure(figsize=(12, 9))
plt.subplot(221)
plt.plot(t, y1)
plt.xlabel('时间/S')
plt.title('信号1 时间域')
plt.subplot(222)
plt.plot(range(400), Y1)
plt.xlabel('频率/Hz')
plt.title('信号1 频率域')
plt.subplot(223)
plt.plot(t, y2)
plt.xlabel('时间/S')
plt.title('信号2 时间域')
plt.subplot(224)
plt.plot(range(400), Y2)
plt.xlabel('频率/Hz')
plt.title('信号2 频率域')
plt.show()
