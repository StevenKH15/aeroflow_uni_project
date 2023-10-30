import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__, name='Data Correlation', title='AuraFlow | Data Correlation')

from assets.fig_layout import my_figlayout, my_linelayout

_data_airp = pd.read_csv('data/datatraining.txt')
_data_airp = _data_airp.rename(columns={'date':'Time'})
_data_airp['Time'] = pd.to_datetime(_data_airp['Time'], errors='raise')


def plot_features(name):
    _data = _data_airp.copy()
    # Plot
    fig_1 = go.Figure(layout=my_figlayout)
    fig_1.add_trace(go.Scatter(x=_data['Time'], y=_data[name], line=dict()))
    fig_1.update_layout(title=name, xaxis_title='Time', yaxis_title='Values')
    fig_1.update_traces(overwrite=True, line=my_linelayout)
    return fig_1

def set_bgcolor(bg_color = "rgb(20, 20, 20)",
                grid_color="rgb(150, 150, 150)", 
                zeroline=False):
    return dict(showbackground=True,
                backgroundcolor=bg_color,
                gridcolor=grid_color,
                color='white',
                zeroline=zeroline)

def plot_3d_scatter():
    data = _data_airp.copy()
    data.Occupancy = data.Occupancy.astype(str)
    #Plot
    fig = px.scatter_3d(
        data,
        x='Temperature',
        y='Humidity',
        z='CO2',
        color='Occupancy',
        color_discrete_map={'1':'#F0FFFF', '0':'#088F8F'},
    )
    fig.update_layout(
        title={'text': "Features and Occupancy",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font':dict(color='white')
        },
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",)
    fig.update_scenes(xaxis=set_bgcolor('#042f33'), 
                  yaxis=set_bgcolor('#042f33'), 
                  zaxis=set_bgcolor('#042f33'))
    return fig

### PAGE LAYOUT ###############################################################################################################

layout = dbc.Container([
    # title
    dbc.Row([
        dbc.Col([html.H3(['Correlation in data'])], width=12, className='row-titles')
    ]),
    # Graphs
    dbc.Row([
        dbc.Col([
            dcc.Loading(id='p2-2-loading', type='circle', children=dcc.Graph(figure=plot_3d_scatter(), id='fig-correlation', className='my-graph'))
        ], width=12, className='multi-graph')
    ]),
    dbc.Row([ 
        dbc.Col([
            dcc.Loading(id='p2-2-loading', type='circle', children=dcc.Graph(figure=plot_features('Temperature'),id='fig-temperature', className='my-graph'))
        ], width=6, className='multi-graph'),
        dbc.Col([
            dcc.Loading(id='p2-2-loading', type='circle', children=dcc.Graph(figure=plot_features('Humidity'),id='fig-humidity', className='my-graph'))
        ], width=6, className='multi-graph')
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Loading(id='p2-2-loading', type='circle', children=dcc.Graph(figure=plot_features('CO2'),id='fig-co2', className='my-graph'))
        ], width = 6, className='multi-graph'),
        dbc.Col([
            dcc.Loading(id='p2-2-loading', type='circle', children=dcc.Graph(figure=plot_features('Light'),id='fig-light', className='my-graph'))
        ], width=6, className='multi-graph')
    ]),
])

