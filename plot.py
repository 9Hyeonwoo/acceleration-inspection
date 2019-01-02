import plotly.plotly as py
import plotly.graph_objs as go
import sys
import pandas as pd

if (len(sys.argv) != 4):
    print("3 argments are needed")
    print("acceleration data file")
    print("location speed & derivative file")
    print("file name")
try:
    acc_file = pd.read_csv(sys.argv[1])
    loc_file = pd.read_csv(sys.argv[2])
except Exception:
    print("cant open file")
    sys.exit(0)

acc = acc_file.values
loc = loc_file.values

moving_index = acc[0,0]

speed_line = go.Scatter(
        x=loc[:, 0] - moving_index,
        y=loc[:, 1],
        name='speed',
        connectgaps=True
        )

der_line = go.Scatter(
        x=loc[:, 0] - moving_index,
        y=loc[:, 2],
        name='derivative',
        connectgaps=True
        )

acc_line = go.Scatter(
        x=acc[:, 0] - moving_index,
        y=acc[:, 1],
        name='acceleration'
        )
data = [speed_line, der_line, acc_line]

fig = dict(data=data)
py.plot(fig, filename=sys.argv[3])
