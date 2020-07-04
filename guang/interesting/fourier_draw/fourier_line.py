import numpy as np
import matplotlib.pyplot as plt
from guang.interesting.fourier_draw.clean_data import get_data_from_func, clean_data
from matplotlib.animation import FuncAnimation

def draw(X, fig, ax, large_to_small = True):
    n = len(X)
    F = np.fft.fft(X)

    F[np.abs(F) < 1] = 0
    N = (np.abs(F) > 0).sum()
    print('总点数{}，过滤后的有效点数{}'.format(n, N))

    # pic_total = ax.plot(X.real, X.imag, linestyle=':', color='gray')  # 完整图像
    # pic_total = ax.plot([0],[0])
    
    # 已经画出来的图像，后面填充
    pic_drawn = ax.plot([0], [0], '-r', linewidth=1.5)
    # n-1个圆周,后面填充
    circle_plt_list = [ax.plot([0], [0], '-', color="lightgrey",linewidth=0.5)[0] for i in range(n - 1)]
    # 直径线，后面填充
    radius_plt = ax.plot([0,0], [0,0], color='r', marker='.', linestyle='-', linewidth=0.7, markersize=3)
    #
    # plt.ion()

    def update_all(xi):
        # fs =
        # w_max =
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

        # return radius_plt

    return update_all


if __name__ == '__main__':
    from matplotlib import animation
    # 导入数据
    X = get_data_from_func()
    # 清洗数据
    X = clean_data(X)
    fig, ax = plt.subplots(1, 1)
    update_all = draw(X, fig, ax, large_to_small=0)
    print(update_all)
    ani = FuncAnimation(fig, update_all, blit=True, interval=10, frames=len(X))
    plt.axis("equal")
    plt.xlim(-0.8, 0.8)
    plt.ylim(-0.8, 0.85)
    # ani.save('fourier.gif', writer='pillow', dpi=200, fps=10)
    ani.save('fourier0.gif', writer='imagemagick',dpi=200, fps=15)

    # ani.save('fourier.avi', writer = animation.FFMpegWriter(),dpi=200, fps=10)

    plt.show()
