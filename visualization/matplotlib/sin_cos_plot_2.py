import numpy as np
import matplotlib.pyplot as plt


def drawSinCosPlot(ax, x, y, label, color, title):
    ax.plot(x, y, label=label, color=color, linewidth=2)
    # X轴和Y轴的刻度范围
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.5, 1.5)
    # 刻度
    x_ticks = np.arange(0, 2 * np.pi + np.pi / 2, np.pi / 2)
    x_ticklabels = [
        r"$0$",
        r"$\frac{\pi}{2}$",
        r"$\pi$",
        r"$\frac{3\pi}{2}$",
        r"$2\pi$",
    ]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticklabels)
    ax.set_aspect("equal")
    ax.set_title(title)
    ax.grid()


x_array = np.linspace(0, 2 * np.pi, 1000)
sin_y = np.sin(x_array)
cos_y = np.cos(x_array)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
drawSinCosPlot(axes[0], x_array, sin_y, "sin", "b", "Sin Function")
drawSinCosPlot(axes[1], x_array, cos_y, "cos", "r", "Cos Function")
plt.tight_layout()
plt.show()
