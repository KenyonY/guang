import numpy as np
import scipy.signal as signal

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


if __name__ == "__main__":
    import plotly.graph_objs as go
    x = np.linspace(0, 1, 10000)
    y = np.sin(2 * np.pi * 20 * x)
    frequency, idx_max, idx_min = culc_frequency(x, y)
    print(frequency)
    fig = go.Figure(go.Scatter(x=x, y=y))
    fig.add_trace(go.Scatter(x=x[idx_max], y=y[idx_max], mode="markers"))
    fig.add_trace(go.Scatter(x=x[idx_min], y=y[idx_min], mode="markers"))
    fig.show()

    