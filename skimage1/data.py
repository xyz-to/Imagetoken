import matplotlib.image as mpimg  # 用于读取图片
import cv2


def cat():
    """返回猫图片"""
    img_brg = cv2.imread('cat.png')
    img_rgb = cv2.cvtColor(img_brg, cv2.COLOR_BGR2RGB)
    return img_rgb


def girl():
    """返回美女图片"""
    image = mpimg.imread('girl.png')
    return image


def house():
    """返回马照片"""
    image = mpimg.imread('house.png')
    return image
