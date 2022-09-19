


import numpy as np
# import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots




n = 1000
x = np.linspace(0, 1, n)
z = 20 * np.sin(2 * np.pi * 3 * x) + 100 * np.exp(x)
error = 10 * np.random.randn(n)
t = z + error




def fourier(M, x):
    arr = []
    for i in range(n):
        arr1 = []
        for j in range(0, M + 1):
            if j == 0:
                arr1.append(1)
            elif j % 2 != 0:
                arr1.append(np.sin((j // 2 + 1) * x[i]))
            else:
                arr1.append(np.cos(j // 2 * x[i]))
        arr.append(arr1)

    return np.array(arr)



def W1(M, x, t):
    arr = fourier(M, x)
    return np.linalg.inv(arr.T @ arr) @ arr.T @ t




def Y1(M, x, t):
    w = W1(M, x, t)
    arr = fourier(M, x)
    y = arr @ w.T
    return y




def pol(M, x):
    arr = []
    for i in range(0, 1000):
        arr1 = []
        for j in range(0, M + 1):
            arr1.append(x[i] ** j)
        arr.append(arr1)

    return np.array(arr)



def W(M, x, t):
    arr = pol(M, x)
    return np.linalg.inv(arr.T @ arr) @ arr.T @ t



def Y(M, x, t):
    w = W(M, x, t)
    arr = pol(M, x)
    y = w @ arr.T
    return y





def plot_1(x, z, t, M):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=z, line={'width': 5}, name='z=20 * np.sin(2 * np.pi * 3 * x) + 100 * np.exp(x)'))
    fig.add_trace(go.Scatter(x=x, y=t, mode='markers', opacity=0.8, name='t=z + error'))
    fig.add_trace(go.Scatter(x=x, y=Y(M, x, t), line={'width': 5}, name='y'))

    fig.show()





plot_1(x, z, t, 1)



plot_1(x, z, t, 8)



plot_1(x, z, t, 100)





def plot_2(x, z, t, M):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=z, line={'width': 5}, name='z=20 * np.sin(2 * np.pi * 3 * x) + 100 * np.exp(x)'))
    fig.add_trace(go.Scatter(x=x, y=t, mode='markers', opacity=0.8, name='t=z + error'))
    fig.add_trace(go.Scatter(x=x, y=Y1(M, x, t), line={'width': 5}, name='y'))
    fig.show()


plot_2(x, z, t, 1)


plot_2(x, z, t, 7)


plot_2(x, z, t, 10)

