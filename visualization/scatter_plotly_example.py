import numpy as np
import plotly.express as px

iris_df = px.data.iris()

fig = px.scatter(
    iris_df,
    x="sepal_length",
    y="sepal_width",
    color="species",
    width=600,
    height=600,
    labels={"sepal_length": "Sepal length(cm)", "sepal_width": "Sepal width(cm)"},
)
fig.update_layout(xaxis_range=[4, 8], yaxis_range=[1, 5])
xticks = np.arange(4, 8 + 1)
yticks = np.arange(1, 5 + 1)
fig.update_layout(xaxis=dict(tickmode="array", tickvals=xticks))
fig.update_layout(yaxis=dict(tickmode="array", tickvals=yticks))
fig.show()
