import numpy as np
import matplotlib.pyplot as plt

x_array = np.linspace(0, 2 * np.pi, 1000)
sin_y = np.sin(x_array)
cos_y = np.cos(x_array)

# 画图绘图区域是一行一列
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
# 折线图
ax.plot(x_array, sin_y, label="sin", color="b", linewidth=2)
ax.plot(x_array, cos_y, label="cos", color="r", linewidth=2)
# 标题
ax.set_title("Sin and Cos Functions")
# X轴和Y轴标签
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
# 图例
ax.legend()
# X轴和Y轴范围
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

# X轴刻度和刻度标签
x_ticks = np.arange(0, 2 * np.pi + np.pi / 2, np.pi / 2)
x_ticklabels = [r"$0$", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"]
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticklabels)
# 设置X轴和Y轴采用相同的比例
ax.set_aspect("equal")
plt.grid()
# plt.savefig("正弦&余弦函数曲线.svg", format="svg")
plt.show()
