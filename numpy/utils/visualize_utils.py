import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm


# 定义二维数组可视化函数
def visualize_2D(array, title, vmax, vmin):
    fig_width = math.ceil(array.shape[1] * 0.5)
    fig_height = math.ceil(array.shape[0] * 0.5)
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    sns.heatmap(
        array,
        vmax=vmax,
        vmin=vmin,
        annot=True,
        fmt=".0f",
        square=True,
        cmap=cm.get_cmap("RdYlBu_r"),
        linewidths=0.5,
        cbar=False,
        yticklabels=False,
        xticklabels=False,
        ax=ax,
    )
    plt.show()


def visualize_1D(array, title):
    fig, ax = plt.subplots()
    colors = cm.RdYlBu_r(np.linspace(0, 1, len(array)))
    for idx in range(len(array)):
        circle_idx = plt.Circle((idx, 0), 0.5, facecolor=colors[idx], edgecolor="w")
        ax.add_patch(circle_idx)
        ax.text(
            idx,
            0,
            s=str(array[idx]),
            horizontalalignment="center",
            verticalalignment="center",
        )
    ax.set_xlim(-0.6, 0.6 + len(array))
    ax.set_ylim(-0.6, 0.6)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    plt.show()


# a = np.array([-3, -2, -1, 0, 1, 2, 3])
# visualize_1D(a, "np.array([-3, -2, -1, 0, 1, 2, 3])")

print(np.array(42, dtype=float))

a_2D = np.array([[-3], [-2], [-1], [0], [1], [2]])
visualize_2D(a_2D, "手动，二维", 3, -3)
