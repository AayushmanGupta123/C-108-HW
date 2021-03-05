import plotly.figure_factory as px
import pandas as pd
import csv

file = pd.read_csv("Data.csv")
fig = px.create_distplot([file["Height(Inches)"].tolist()], ["Height"],show_hist = False)
fig.show()