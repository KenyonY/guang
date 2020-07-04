import numpy as np



def get_data_from_func():
    '''
    心图作为 demo
    :return:
    '''
    n = 150
    t = np.linspace(0, 2 * np.pi, n)
    x = 16 * (np.sin(t)) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    X = x + 1j * y
    return X

def get_data_from_pic():
    pass


def get_data_from_csv():
    pass

def sort_data(X):
    '''
    对于图数据，使用最短路径算法得到序列。
    然后返回二元数(2维)或三元数(三维)形式
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
