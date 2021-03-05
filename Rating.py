import plotly.figure_factory as px
import pandas as pd
import csv

Df = pd.read_csv("data1.csv")
fig = px.create_distplot([Df["Avg Rating"].tolist()], ["Avg Rating"],show_hist = False)
fig.show()