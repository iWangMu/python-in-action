import plotly.express as px
import numpy as np

x = np.linspace(0, 2 * np.pi, 1000)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig = px.line(x=x, y=[y_sin, y_cos], labels={"x": "x", "y": "f(x)"})
fig.data[0].name = "Sine"
fig.data[1].name = "Cosine"
fig.show()
