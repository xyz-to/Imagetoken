"""图像颜色矩"""

from skimage import data
import numpy as np
from scipy import stats

img = data.coffee()

features = np.zeros((3, 3))

for k in range(3):
    # 平均值
    mu = np.mean(img[:, :, k])
    # 方差
    delta = np.std(img[:, :, k])
    # 偏移值
    skew = np.mean(stats.skew(img[:, :, k]))
    features[k, 0] = mu
    features[k, 1] = delta
    features[k, 2] = skew

print(features)