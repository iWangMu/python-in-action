import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle

for num_vertices in range(3, 9):
    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot()

    ax.set_aspect("equal")
    hexagon_inner = RegularPolygon(
        (0, 0), numVertices=num_vertices, radius=1, alpha=0.2, edgecolor="k"
    )
    ax.add_patch(hexagon_inner)

    plt.axis("off")

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.show()
