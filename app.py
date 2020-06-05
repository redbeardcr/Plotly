import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

countcompany = pd.read_csv('..\Data\countcompany.csv')

df = pd.pivot_table(countcompany, index='CompanyStatusLabel',
                    values='n', aggfunc=sum)
print(df)

data = [go.Bar(
    x=df.index,
    y=df.values,
)]

layout = go.Layout(title='Title')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
