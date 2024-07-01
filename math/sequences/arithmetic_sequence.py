import numpy as np
import matplotlib.pyplot as plt

# 1, 2, 3, ..., 100
a = 1
d = 1
n = 100
AP_sequence = np.arange(a, a + n * d, d)
index = np.arange(1, n + 1, 1)

fig = plt.figure(figsize=(16, 8))
ax_1 = fig.add_subplot(2, 1, 1)
# 序列值
ax_1.set_xlabel("Index, k")
ax_1.set_ylabel("Term, $a_k$")
ax_1.stem(index, AP_sequence)
ax_1.grid(linestyle="--", linewidth=0.25, color=[0.5, 0.5, 0.5])
ax_1.set_xlim(index.min() - 1, index.max() + 1)
ax_1.set_ylim(0, AP_sequence.max() + 10)
ax_1.spines["right"].set_visible(False)
ax_1.spines["top"].set_visible(False)
# 求和
cumsum_AP = np.cumsum(AP_sequence)
ax_2 = fig.add_subplot(2, 1, 2)
ax_2.set_xlabel("Index, k")
ax_2.set_ylabel("Cumulative sum, $S_k$")
ax_2.stem(index, cumsum_AP)
ax_2.grid(linestyle="--", linewidth=0.25, color=[0.5, 0.5, 0.5])
ax_2.set_xlim(index.min() - 1, index.max() + 1)
ax_2.set_ylim(0, cumsum_AP.max() + 100)
ax_2.spines["right"].set_visible(False)
ax_2.spines["top"].set_visible(False)

plt.show()
