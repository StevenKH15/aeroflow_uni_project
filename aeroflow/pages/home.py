import os
import dash
import base64
import pandas as pd
from pages.utils import *
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from assets.fig_layout import my_figlayout, my_linelayout
from dash import html, dcc, callback, Input, Output, State

dash.register_page(__name__, path='/', name='Home', title='AuraFlow | Home', redirect_from=["/home"])

LOGO = os.path.join(os.getcwd(), "images/logo.png")
test_base64 = base64.b64encode(open(LOGO, 'rb').read()).decode('ascii')
purpose_img = base64.b64encode(open(os.path.join(os.getcwd(), "images/purpose.png"), 'rb').read()).decode('ascii')
live_data_img = base64.b64encode(open(os.path.join(os.getcwd(), "images/live_data.png"), 'rb').read()).decode('ascii')
historical_data_img = base64.b64encode(open(os.path.join(os.getcwd(), "images/historical_data.png"), 'rb').read()).decode('ascii')
predictions_img = base64.b64encode(open(os.path.join(os.getcwd(), "images/predictions.png"), 'rb').read()).decode('ascii')
data_correlation_img = base64.b64encode(open(os.path.join(os.getcwd(), "images/data_correlation.png"), 'rb').read()).decode('ascii')

### PAGE LAYOUT ###############################################################################################################

layout = dbc.Container([
    # title
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Br(),
            # html.H1([html.B('AuraFlow')]),
            html.Img(src='data:image/png;base64,{}'.format(test_base64), height="100px", width="100px", style={'opacity':1, 'align':'center'}),
        ], width=11, className='row-titles')
    ]),

    # data input
    dbc.Col([
        dbc.Row([
            # dbc.Col([], width = 1),
            dbc.Col([dbc.Card([dbc.CardImg(src='data:image/png;base64,{}'.format(purpose_img))])], width=9),
            dbc.Col([
                dbc.Card([
                    dbc.Button([
                        dbc.CardImg(src='data:image/png;base64,{}'.format(live_data_img))],
                        className='my-card-forward',
                        href="./step1",),]),
                dbc.Card([
                    dbc.Button([
                        dbc.CardImg(src='data:image/png;base64,{}'.format(historical_data_img))],
                        className='my-card-forward',
                        href="./step2",),]),
                dbc.Card([
                    dbc.Button([
                        dbc.CardImg(src='data:image/png;base64,{}'.format(data_correlation_img))],
                        className='my-card-forward',
                        href="./step3",),]),
                dbc.Card([
                    dbc.Button([
                        dbc.CardImg(src='data:image/png;base64,{}'.format(predictions_img))],
                        className='my-card-forward',
                        href="./step4",),]),
                ], width=2)
        ], className='row-content'),

        dbc.Row([
            dbc.Col([], width = 1),
            dbc.Col([
                create_purpose_card(test_base64, 'Purpose'),
            ], width=3),
            dbc.Col([
                create_purpose_card(test_base64, 'Introduction'),
            ], width=3),
            dbc.Col([
                create_purpose_card(test_base64, 'Objectives'),
            ], width=3),
        ], className='row-content'),

        dbc.Row([
            dbc.Col([], width = 1),
            dbc.Col([
                create_purpose_card(test_base64, 'Expected Results'),
            ], width = 6),
            dbc.Col([
                create_purpose_card(test_base64, 'Background'),
            ], width=3),
        ], className='row-content'),
    ])
])

### PAGE CALLBACKS ###############################################################################################################

@callback(
    Output("collapse_Purpose", "is_open"),
    [Input("collapse-button-Purpose", "n_clicks")],
    [State("collapse_Purpose", "is_open")],
)
def toggle_collapse_purpose(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output("collapse_Introduction", "is_open"),
    [Input("collapse-button-Introduction", "n_clicks")],
    [State("collapse_Introduction", "is_open")],
)
def toggle_collapse_purpose1r(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    Output("collapse_Objectives", "is_open"),
    [Input("collapse-button-Objectives", "n_clicks")],
    [State("collapse_Objectives", "is_open")],
)
def toggle_collapse_purpose2(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    Output("collapse_Expected Results", "is_open"),
    [Input("collapse-button-Expected Results", "n_clicks")],
    [State("collapse_Expected Results", "is_open")],
)
def toggle_collapse_purpose3(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    Output("collapse_Background", "is_open"),
    [Input("collapse-button-Background", "n_clicks")],
    [State("collapse_Background", "is_open")],
)
def toggle_collapse_purpose4(n, is_open):
    if n:
        return not is_open
    return is_open