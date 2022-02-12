#!/usr/bin/python

import tonic
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import tonic.transforms as transforms
from matplotlib.animation import FuncAnimation

def init():
    ax.set_xlim(0,32)
    ax.set_ylim(0,32)  
    point.set_data([], [])
    return point,

def animate(i, t_numpy, x_numpy, y_numpy, p_numpy):
    if i == t_numpy[i]:
        ax.set_data(10,10)
        print(t_numpy[i])
        if p_numpy[i] == 0:
            print(p_numpy[i])
            ax.set_data(10,10)
            ax.set_data(x_numpy[i], y_numpy[i])
            # point.set_color('k')
            print(x_numpy[i], y_numpy[i])
        elif p_numpy[i] == 1:
            # point.set_color('w')
            point.set_data(x_numpy[i], y_numpy[i])
    return point,

sensor_size_p = 2
sensor_size_x = 32
sensor_size_y = 32

sensor_size = (sensor_size_x, sensor_size_y, sensor_size_p)

datasets = tonic.datasets.POKERDVS(save_to='./data', train=True)
datapoints, target = datasets[40]

df = pd.DataFrame(datapoints, columns = ['t','x','y','p'])
p_numpy = df['p'].to_numpy()
t_numpy = df['t'].to_numpy()
df.set_index('t', inplace=True)
x_numpy = df['x'].to_numpy()
y_numpy = df['y'].to_numpy()

print('Poker card label (int): ', target)
print('coordinate points (events): ', datapoints)

transformEvents = transforms.ToFrame(sensor_size = sensor_size, event_count = len(datapoints)//10, overlap=0.01)

framess = transformEvents(datapoints)
print('framess', framess)

fig, ax = plt.subplots()
fig1, axes = plt.subplots(1,2)
point, = ax.plot([],[], markersize = 50)
ax.patch.set_facecolor('tab:gray')
ax.set_xlim(0,32)
ax.set_ylim(0,32)


print(point)

time_points = sns.scatterplot(ax=axes[0], x="x", y="y", data=df, hue=df.index)
polarity_points = sns.scatterplot(ax=axes[1], x="x", y="y", data=df, hue="p", palette = 'Greys')

animation = FuncAnimation(fig, animate, frames = range(df.index[0], df.index[-1], 1), 
                          init_func = init, fargs = [t_numpy, x_numpy, y_numpy, p_numpy], interval = 10)

plt.show()