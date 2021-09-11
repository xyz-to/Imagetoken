from skimage import io
from matplotlib import pyplot as plt
from image_take import change_alpha
from skimage import data

"""图片的读取操作"""
file_name = 'girl.png'
image = io.imread(fname=file_name)
print(image.shape)

"""图片显示"""
plt.imshow(image)
plt.show()

"""改变图片对比度"""
plt.imshow(change_alpha(data.coffee(), 0.5))
plt.show()
