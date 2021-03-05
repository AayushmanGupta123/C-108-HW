import random
import plotly.figure_factory as px
dice = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1 + dice2)

fig = px.create_distplot([dice],["Result"])
fig.show()