import numpy as np
import matplotlib.pyplot as plt
from compose import get_data_from_func, clean_data, from_text
from matplotlib.animation import FuncAnimation

from matplotlib import rc
# rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
# rc('text', usetex=True)
# plt.style.use(["science"])

major_tick_dict = dict(which='major', direction='in', top=1, right=1, length=5, width=0.3, labelsize=10)
minor_tick_dict = dict(which='minor', direction='in', top=1, right=1, length=3, width=0.2, labelsize=10)

def draw(X, fig, ax, large_to_small = True):
    n = len(X)
    F = np.fft.fft(X)

    F[np.abs(F) < 10] = 0
    N = (np.abs(F) > 0).sum()
    print('总点数{}，过滤后的有效点数{}'.format(n, N))

    pic_total = ax.plot(X.real, X.imag, linestyle=':', color='gray')  # 完整图像
    pic_total = ax.plot([0],[0])
    
    # 已经画出来的图像，后面填充
    pic_drawn = ax.plot([0], [0], '-r', linewidth=1.2)
    # n-1个圆周,后面填充
    circle_plt_list = [ax.plot([0], [0], '-', color="lightgrey",linewidth=0.5)[0] for i in range(n - 1)]
    # 直径线，后面填充
    radius_plt = ax.plot([0,0], [0,0], color='r', marker='.', linestyle='-', linewidth=0.7, markersize=3)
    #
    # ax.set_xlim(0, 1000)
    # ax.set_ylim(-0.5, 0.5)
    plt.ion()

    def update_part(xi):

        w = 2 * np.pi * np.arange(n) / n
        dw = 1/n
        Fedw = F * np.exp(1j *xi * w) * dw


        if large_to_small:
            # sort from largest to smallest
            idx = np.argsort(abs(Fedw))[-1:-N-1:-1]
            radius_points = np.cumsum(Fedw[idx]) # Fedw

        else:
            # sort from smallest to largest
            idx = np.argsort(abs(Fedw))[n-N:]
            # M = N
            radius_points = np.cumsum(Fedw[idx])
        radius_points = np.insert(radius_points, 0, 0 + 0j)


        plt.setp(radius_plt[0], 'xdata', radius_points.real, 'ydata', radius_points.imag)
        plt.setp(pic_drawn, 'xdata', X[:int(xi) + 1].real, 'ydata', X[:int(xi) + 1].imag)  # 已经画出来的图像，用真实值
        plt.setp(radius_plt[0], 'xdata', radius_points.real, 'ydata', radius_points.imag)  # 直径线

        # N个圆周：
        for j in range(N):
            center, radius = radius_points[j], F[idx[j]]
            circle_point = center + radius * np.exp(1j * np.linspace(0, 2 * np.pi, 60)) / n
            plt.setp(circle_plt_list[j], 'xdata', circle_point.real, 'ydata', circle_point.imag)
        return pic_drawn + radius_plt + circle_plt_list

    return update_part

def hyeves(data, large_to_small=1, fps=12):
    fig, ax = plt.subplots(1, 1, figsize=(7,5))
    plt.minorticks_on()
    ax.tick_params(**major_tick_dict)
    ax.tick_params(**minor_tick_dict)
    # for X in data:
    X = data[0]
    # print(X, X.shape)
    # plt.plot(X.real, X.imag)
    update_part = draw(X, fig, ax, large_to_small=large_to_small)
    ani = FuncAnimation(fig, update_part, blit=True, interval=10, frames=len(X))

    plt.axis("equal")
    # plt.xlim(-1000, 1000)
    # plt.xlim(-0.8, 0.8)
    # plt.ylim(-0.8, 0.85)

    # plt.axis('off')
    # plt.xticks([])
    # plt.yticks([])

    # ani.save(f'fourier{large_to_small}.gif', writer='pillow', dpi=10, fps=fps)

    # ani.save(f'fourier{large_to_small}.gif', writer='imagemagick',dpi=200, fps=fps)

    # ani.save('fourier.avi', writer = animation.FFMpegWriter(),dpi=200, fps=10)
    plt.show()
if __name__ == '__main__':
    # X = get_data_from_func()
    # hyeves(X, 1)
    # hyeves(X, 0)
    data = from_text("533", 2)
    hyeves(data)
