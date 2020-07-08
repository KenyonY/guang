from manimlib.imports import *
import numpy as np
import imageio
from skimage import measure, filters
import matplotlib.pyplot as plt
from guang import rm

# from PIL import Image
# from guang import path
# from skimage.transform import hough_circle, hough_circle_peaks
# from skimage.feature import canny
# import cv2
# from guang import implot, auto_canny



def from_func():
    '''
    love function
    '''
    n = 150
    t = np.linspace(0, 2 * np.pi, n)
    x = 16 * (np.sin(t)) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    X = x + 1j * y
    return X

def from_text(S = "LOVE", scale=2, style=None):
    """get text contour list
    """
    text = TextMobject(S).scale(scale)
    img = text.get_image()
    gray_img = np.array(img.convert("L"))
    contours = measure.find_contours(gray_img, 120)

    except_list = ["*.aux", "*.log", "*.svg", "*.tex", "*.xdv"]
    print(f"Deleting {except_list} in directory \n{os.getcwd()}")
    [rm(i) for i in except_list]
    X = []
    for contour in contours:
        x, y = contour[:, 1], -contour[:, 0]
        X.append(x+1j*y)
    return X



def from_pic():
    pass


def from_csv():
    pass

def sort_data(X):
    '''
    对于图数据，使用最短路径算法得到序列。
    然后返回二元数(2维)或三/四元数(三维)形式
    其定义在guang.geo.space中
    '''
    return X


def clean_data(X):
    
    X = sort_data(X)
    x, y = X.real, X.imag
    x = (x - x.min()) / (x.max() - x.min()) - 0.5
    y = (y - y.min()) / (y.max() - y.min()) - 0.5
    X = x + 1j * y
    return X

if __name__ == "__main__":
    pass
    # X = from_text("533", 5)
    # plt.figure(figsize=(10, 5))
    # for x in X:
    #     plt.plot(x.real, x.imag, linewidth=2)
    # plt.axis("equal")

