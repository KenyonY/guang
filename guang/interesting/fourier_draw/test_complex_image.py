import numpy as np
import matplotlib.pyplot as plt
def get_data_from_func():
    '''
    心图作为 demo
    :return:
    '''
    n = 1000
    t = np.linspace(0, 2 * np.pi, n)
    x = 16 * (np.sin(t)) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    X = x + 1j * y
    return X



def circle(r, n):
    theta = np.linspace(0, np.pi * 2, n)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    X = x + y * 1j
    return X


n = 300
X = circle(10, n)
FX = np.fft.fft(X)
XX = np.fft.ifft(FX)
for w in range(1,5):

    plt.figure()
    # plt.plot(right.real[:n//2], right.imag[:n//2])
    # plt.axis("equal")
    # plt.show()
    fxright = FX * np.exp(w * 1j * 2 * np.pi * np.arange(n) / n) # 逆变换，根据正交性就只取到w频率的振幅
    radius_points = np.cumsum(fxright) / n

    plt.plot(fxright.real, fxright.imag)
    plt.show()

    for j in range(n - 1):
        center, radius = radius_points[j], FX[j + 1]
        circle_point = center + radius * np.exp(1j * np.linspace(0, 2 * np.pi, 30)) / n

# plt.figure()
# plt.plot(X.real[:], X.imag[:])
# plt.axis("equal")
# plt.show()
