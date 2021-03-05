import plotly.figure_factory as px
import pandas as pd
import csv

Datafile = pd.read_csv("Data.csv")
fig = px.create_distplot([Datafile["Weight(Pounds)"].tolist()], ["Weight(Pounds)"],show_hist = False)
fig.show()