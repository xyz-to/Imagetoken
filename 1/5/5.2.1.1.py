"""灰度共生矩阵"""

import matplotlib.pyplot as plt
from skimage import data
from skimage.feature import greycomatrix, greycoprops
from pylab import mpl

"""中文显示工具"""
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

PATCH_SIZE = 21

img = data.camera()
# 选择四个草地区域块
grass_locations = [(474, 291), (440, 433), (466, 18), (462, 236)]
grass_patches = []
for loc in grass_locations:
    grass_patches.append(img[loc[0]:loc[0] + PATCH_SIZE, loc[1]:loc[1] + PATCH_SIZE])

# 选择四个天空区域块
sky_locations = [(54, 48), (21, 233), (90, 380), (195, 330)]
sky_patches = []
for loc in sky_locations:
    sky_patches.append(img[loc[0]:loc[0] + PATCH_SIZE, loc[1]:loc[1] + PATCH_SIZE])

# 灰度共生矩阵
xs = []
ys = []
for patch in (sky_patches + grass_patches):
    # 参数：距离，方向，是否对称，是否标准化
    glcm = greycomatrix(patch, [5], [0], 256, symmetric=True, normed=True)  # 得到的矩阵，行表示距离，列表示角度
    xs.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    ys.append(greycoprops(glcm, 'correlation')[0, 0])

# 显示
fig = plt.figure()
ax = fig.add_subplot(121)
ax.imshow(img, 'gray')
for y, x in grass_locations:
    ax.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'gs')
for y, x in sky_locations:
    ax.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'ws')
ax.set_xlabel('原始图像')

ax = fig.add_subplot(122)

ax.plot(xs[:len(grass_locations)], ys[:len(grass_locations)], 'go', label='Grass')
ax.plot(xs[:len(sky_patches)], ys[:len(sky_locations)], 'bo', label='Grass')
plt.show()
