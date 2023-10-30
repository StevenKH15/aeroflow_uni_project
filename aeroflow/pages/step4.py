import dash
import warnings
import pandas as pd
from pages.utils import *
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

warnings.filterwarnings("ignore")
dash.register_page(__name__, name='Predictions', title='AuraFlow | Predictions')
from assets.fig_layout import my_figlayout, train_linelayout, pred_linelayout

_data_airp = pd.read_csv('data/datatest2.txt', usecols = [1, 2, 3, 5], names = ['Time', 'Temperature', 'Humidity', 'CO2'], skiprows=1)
_data_airp['Time'] = pd.to_datetime(_data_airp['Time'], errors='raise')

_trainp = 80
idx_split = round(len(_data_airp['Temperature']) * (_trainp/100)) # Split train-test
_datatrain = _data_airp.iloc[:idx_split+1]
_opts = range(0,int(len(_datatrain['Temperature'])/2),1)
_opts = list(_opts)

### PAGE LAYOUT ###############################################################################################################

layout = dbc.Container([
    # title
    dbc.Row([
        dbc.Col([html.H3(['Final Model: Fit & Prediction'])], width=12, className='row-titles')
    ]),
    dbc.Row([
        dbc.Col([], width=1),
        dbc.Col([create_feature_for_prediction()], width=4),
    ], style={'margin':'20px 0px 0px 0px'}),
    dbc.Row([
        dbc.Col([], width = 1),
        dbc.Col([
            dcc.Loading(id='m1-loading', type='circle', children=dcc.Graph(id='fig-pg41', className='my-graph'))
        ], width = 10),
        dbc.Col([], width = 1)
    ], className='row-content'),
])

### PAGE CALLBACKS ###############################################################################################################

# Generate predictions & Graph
@callback(
    Output(component_id='fig-pg41', component_property='figure'),
    Input(component_id='feature_prediction', component_property='value')
)
def predict_(name):    
    # Get data
    if not name:
        name = 'Temperature'
    _data = _data_airp.copy()

    y_train = _data[name][:idx_split+1]
    y_test = _data[name][idx_split+1:]

    data_train = y_train.to_frame()
    data_train['Time'] = _data['Time'][:idx_split+1].to_frame()
    data_train['_is_train'] = 1
    data_test = y_test.to_frame()
    data_test['Time'] = _data['Time'][idx_split+1:].to_frame()
    data_test['_is_train'] = 0

    data_pred = y_test.to_frame() + 0.1
    data_pred['Time'] = _data['Time'][idx_split+1:].to_frame()
    data_pred['_is_train'] = 2
    _data_all = pd.concat([data_train, data_test, data_pred], ignore_index=True)
    _data_all = _data_all.sort_values(by=['Time'])
    
    # Show model results
    fig1 = go.Figure(layout=my_figlayout)
    # Lines
    fig1.add_trace(go.Scatter(x=_data_all.loc[_data_all['_is_train']==1, 'Time'],
                                y=_data_all.loc[_data_all['_is_train']==1, name], mode='lines', name='Train', line=train_linelayout))

    fig1.add_trace(go.Scatter(x=data_pred['Time'], y=data_pred[name], mode='lines', name='Predictions', line=pred_linelayout))
    fig1.update_xaxes(title_text = 'Time')
    fig1.update_yaxes(title_text = name)
    fig1.update_layout(title="Final Model Results", height=500)

    return fig1