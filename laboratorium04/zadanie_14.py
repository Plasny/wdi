#!/usr/bin/env python3

from matplotlib.lines import Line2D

import matplotlib.pyplot as plt
import pandas as pd


def color(species: str):
    match species:
        case 'Iris-virginica': return 'blue'
        case 'Iris-setosa': return 'green'
        case 'Iris-versicolor': return 'red'
        case _: return 'black'


def add_legend():
    plt.legend(handles=[
        Line2D([0], [0], marker='o', color='w', markerfacecolor='blue',
               markersize=10, label='Iris-versicolor'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='red',
               markersize=10, label='Iris-virginica'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='green',
               markersize=10, label='Iris-setosa'),
    ])


df = pd.read_csv('./iris.csv')
colors = [color(v) for v in df['class']]

for col in filter(lambda c: c != 'class', df):
    df.reset_index().plot.scatter(x='index', y=col, color=colors)
    add_legend()

plt.show()
