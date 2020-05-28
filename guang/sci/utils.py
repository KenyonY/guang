import numpy as np
import scipy.signal as signal
from guang.sci.fft import space2fre_2d


def culc_frequency(x, y):
    idx_max = signal.argrelextrema(y, np.greater)[0]
    idx_min = signal.argrelextrema(y, np.less)[0]
    Lmax, Lmin = len(idx_max), len(idx_min)

    if Lmax > Lmin:
        N = Lmax-1
        frequency = N/(x[idx_max[-1]] - x[idx_max[0]])
    else:
        N = Lmin - 1
        frequency = N / (x[idx_min[-1]] - x[idx_min[0]])
    return frequency, idx_max, idx_min


def culc_fig_fre(mat, method, dw=1,  dh=1, fre_min=1., FRE_MAX=15):
    """
    :param mat: 2d array
    :param method: options "1d" or "2d"
    """
    if method == "1d":
        Nh, Nw = mat.shape
        fre_max = 1 / (2 * dw)
        def get_fre(N):
            delta_fre = 2 * fre_max / N
            if N % 2 == 0:
                fre = np.linspace(-fre_max, fre_max, N) - delta_fre / 2
            else:
                fre = np.linspace(-fre_max, fre_max, N)
            idx = np.argwhere(fre >= 0)
            return idx, fre[idx]
        # idx_h, fre_h = get_fre(dh, Nh)
        idx_w, fre_w = get_fre(Nw)
        IDX = np.argwhere(fre_w > FRE_MAX)[0][0]
        F = np.fft.fft2(mat)
        F[:,IDX:-IDX] = 1e-14 + 0j # F[IDX:-IDX, :]
        Fu = F[0, :] # F[:,0]
        res = np.real(np.fft.ifft(Fu))

        x = np.arange(0, dw*Nw, dw)
        # x = np.linspace(0, dw*Nw, Nw)
        # fig = plt.figure()
        # plt.plot(x, res)
        # plt.show()
        frequncy = culc_frequency(x, res)[0]

    elif method == "2d":
        x, y, amplitude = space2fre_2d(mat, dh, dw)
        argmat = x > fre_min
        frequncy = x[argmat][np.argmax(amplitude[argmat])]
    else:
        raise ValueError("bad method")
    return frequncy



if __name__ == "__main__":
    from guang.cv.video import getFrame
    import matplotlib.pyplot as plt
    INFO, mat = getFrame(r'C:\Users\beidongjiedeguang\Desktop\实验\60degree\1_resample.avi', 1400,
                         W=(52, 618), H=(43, 580),
                         gray=1)
    fig2 =plt.figure()
    plt.imshow(mat)
    plt.show()

    dtheta = 3
    dx = dtheta / (618 - 52)
    print(culc_fig_fre(mat, method=1, dw=dx, FRE_MAX=13))
    print(culc_fig_fre(mat, method=2, dw=dx, fre_min=3))

    