import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

countcompany = pd.read_csv(
    'https://raw.githubusercontent.com/redbeardcr/Plotly/master/Data/countcompany.csv')

# df = pd.pivot_table(countcompany, index='CompanyStatusLabel',
#                     values='n', columns='CompanySizeId', aggfunc=sum)
df = pd.pivot(countcompany, index='CompanyStatusLabel',
              values='n', columns='CompanySizeId')
print(df)


# data = [go.Bar(
#     x=df.index,
#     y=df.values.flatten(),
# )]

# layout = go.Layout(title='Title')

# fig = go.Figure(data=data, layout=layout)

# pyo.plot(fig)
