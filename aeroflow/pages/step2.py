import dash
import pandas as pd
from pages.utils import *
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output
dash.register_page(__name__, name='Historical Data', title='AuraFlow | Historical Data')

from assets.fig_layout import my_figlayout, my_linelayout

_data_airp = pd.read_csv('data/datatest2.txt')
_data_airp = _data_airp.rename(columns={'date':'Time'})
_data_airp['Time'] = pd.to_datetime(_data_airp['Time'], errors='raise')

_data_airp_2 = pd.read_csv('data/datatraining.txt')
_data_airp_2 = _data_airp_2.rename(columns={'date':'Time'})
_data_airp_2['Time'] = pd.to_datetime(_data_airp['Time'], errors='raise')

### PAGE LAYOUT ###############################################################################################################

layout = dbc.Container([
    # title
    dbc.Row([
        dbc.Col([html.H3(['Data Visualization'])], width=10, className='row-titles')
    ]),

    # data input
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([
            create_card_for_selection(),
        ], width=4),
        dbc.Col([
            create_feature_for_selection(_data_airp.columns.tolist()[1:]),
        ], width=5),
    ], className='row-content'),

    # raw data fig
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([
            dcc.Loading(id='p1_1-loading', type='circle', children=dcc.Graph(id='fig-pg1', className='my-graph'))
        ], width = 9),
        dbc.Col([], width = 2)
    ], className='row-content')
    
])

### PAGE CALLBACKS ###############################################################################################################

# Update fig
@callback(
    Output(component_id='fig-pg1', component_property='figure'),
    Input(component_id='d2-dropdown', component_property='value'),
    Input(component_id='feature_dropdown', component_property='value'),
)
def plot_data(value, feature):
    fig = None

    if value == 'NTUT - LIBRARY':
        _data = _data_airp
    elif value == 'NTUT - ROOM 424':
        _data = _data_airp_2

    fig = go.Figure(layout=my_figlayout)
    fig.add_trace(go.Scatter(x=_data['Time'], y=_data[feature], line=dict()))

    fig.update_layout(title='Dataset Linechart', xaxis_title='Time', yaxis_title=feature, height = 500)
    fig.update_traces(overwrite=True, line=my_linelayout)

    return fig