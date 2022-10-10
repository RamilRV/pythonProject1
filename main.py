import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots



np.random.seed(11)
height_fut =np.random.randn(500) * 20 + 160
height_fut =np.array(height_fut)
height_bas =np.random.randn(500) * 10 + 190
height_bas =np.array(height_bas)




arr_precision =[]
arr_recall =[]
arr_acc =[]




for height in range(0 ,231):
    TP =0 # баскетбол
    TN =0 # футбол
    FP =0 # футболисты которых записали в баскетбол
    FN =0 # баскетбол которых записали в футбол
    TP = np.sum(height_bas >height)
    FN = len(height_bas) - TP
    TN = np.sum(height_fut <height)
    FP = len(height_fut) - TN
    if TP +FP==0:
        break
    else:
        arr_precision.append(TP /(TP +FP))
        arr_recall.append(TP /(TP +FN))
        arr_acc.append((TP +TN) /(TP +TN +FP+FN))



fig = px.scatter(x=arr_recall, y=arr_precision,
                 hover_data={"accuracy" :arr_acc,
                             "threshold" :range(0 ,len(arr_precision))},

                 )
fig.update_traces(mode="lines")
fig.show()


np.trapz(arr_precision ,arr_recall) * -1 # так как arr_recall сортирован в обратном порядке(уменьшается),
# по этой причине нам необходимо взять значение площади с обратным знаком


# Альтернативный способ нахождения площади
S= 0
for i in range(0, len(arr_precision) - 1):
    h = arr_recall[i + 1] - arr_recall[i]
    S += np.absolute(h) * (arr_precision[i] + arr_precision[i + 1]) / 2
S

