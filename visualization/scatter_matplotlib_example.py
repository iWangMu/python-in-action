import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
iris = load_iris()
print(iris)
sepal_length = iris.data[:, 0]
sepal_width = iris.data[:, 1]
target = iris.target

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(sepal_length, sepal_width, c=target, cmap="rainbow")

ax.set_title("Iris sepal length vs width")
ax.set_xlabel("Sepal length (cm)")
ax.set_ylabel("Sepal width (cm)")

ax.set_xticks(np.arange(4, 9, 1))
ax.set_yticks(np.arange(1, 6, 1))
ax.axis("scaled")

ax.grid(linestyle="--", linewidth=0.25, color=[0.7, 0.7, 0.7])

ax.set_xbound(lower=4, upper=8)
ax.set_ybound(lower=1, upper=5)

plt.show()
