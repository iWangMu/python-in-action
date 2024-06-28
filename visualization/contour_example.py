import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
# 绘制等高线图
plt.contour(X, Y, Z, levels=np.linspace(0, 8, 16 + 1), cmap="RdYlBu_r")
# 添加颜色图例
plt.colorbar()
# 显示图形
plt.show()
