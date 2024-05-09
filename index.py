import plotly
import plotly.graph_objects as go
import pandas as pd
df1 = pd.read_csv('agency_data.csv')
df2 = pd.read_csv('hour_data.csv')
fig = go.Figure()
fig.add_trace(go.Bar(x=df2['Hour'], y=df2['passenger_count'], name='Total Passenger Count',
              hovertemplate='Total Passenger Count: %{y}<extra></extra>'))
for agency in df1['agency'].unique():
    agency_data = df1[df1['agency'] == agency]
    fig.add_trace(go.Scatter(x=agency_data['Hour'], y=agency_data['passenger_count'],
                  mode='lines+markers', name=agency, hovertemplate=f'{agency}: %{{y}}<extra></extra>'))
fig.update_layout(title='Hourly Passenger Flow', xaxis=dict(title='Hour of the Day', tickangle=-45),
                  yaxis=dict(title='Passenger Count', tickformat=','), hovermode='x unified')
fig.show()
