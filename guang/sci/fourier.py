import numpy as np
from numpy.fft import fft,fft2, fftshift


def space2fre(x, y):
    """ Transform space domain (x, y) to the frequency domain (frequency, amplitude)
    """
    x, y = x.reshape(-1, 1)[...,-1], y.reshape(-1, 1)[...,-1]
    x_max = x.max()
    x_min = x.min()
    N = len(x)
    delta_x = (x_max - x_min) / (N - 1)
    f_max = 1 / (2 * delta_x)
    delta_f = 2 * f_max / (N - 1)
    if N%2==0:
        fre_x = np.linspace(-f_max, f_max, N)-delta_f/2
    else:
        fre_x = np.linspace(-f_max, f_max, N)
    fre_y_shift = fftshift(fft(y))
    magnitude_energy = np.abs(fre_y_shift) / (N - 1)
    amplitude_y = magnitude_energy * 2 #  则表示原来振幅
    idx = np.argwhere(fre_x>=0)
    return fre_x[idx].reshape(-1, 1), amplitude_y[idx].reshape(-1, 1)


def space2fre_2d(mat, dh=1, dw=1):
    """mat: 2d numpy array"""

    Nh, Nw = mat.shape
    def get_fre(dx, N):
        fre_max = 1 / (2 * dx)
        # print("fre_max", fre_max)
        delta_fre = 2 * fre_max / N
        if N % 2 == 0:
            fre = np.linspace(-fre_max, fre_max, N) - delta_fre / 2
        else:
            fre = np.linspace(-fre_max, fre_max, N)
        idx = np.argwhere(fre >= 0)
        return idx, fre[idx]
    idx_h, fre_h = get_fre(dh, Nh)
    idx_w, fre_w = get_fre(dw, Nw)
    x, y = np.meshgrid(fre_w, fre_h)
    F = fftshift(fft2(mat))
    magnitude_energy = np.abs(F) / ((Nh - 1) * (Nw - 1))
    amplitude = magnitude_energy * 2
    return x, y, amplitude[idx_h][:, -1, :][:, idx_w][:, :, -1]