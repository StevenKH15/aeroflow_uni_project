import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State

def create_purpose_card(image, name):
    _img = html.Img(src='data:image/png;base64,{}'.format(image), height="100px", width="100px", style={'opacity':1, 'align':'center'})
    purpose = dbc.Card(
        [
            dbc.Button(html.Div([
                html.Br(),
                html.Br(),
                html.H6('{}'.format(name)),
                html.Br(),
                html.Br()], className="card-title"), id="collapse-button-{}".format(name), n_clicks=0, className='my-purpose'),
            dbc.Collapse(
                html.Div(
                    dbc.CardBody(
                                get_info(name)
                            ),
                    style={'background-image': 'linear-gradient(109.6deg, rgb(0, 0, 0) 11.2%, rgb(4, 47, 51) 91.1%)'}
                    # style={'background-image': 'linear-gradient(109.6deg, rgb(0, 0, 0) 11.2%, rgb(56, 185, 233) 91.1%)'}
                ),
                id="collapse_{}".format(name),
                is_open=False,
            )
        ], 
        style={"border": "none"},
        inverse=True,
    )
    return purpose

def get_info(name):
    if name == 'Purpose':
        return  html.P([
                "Step into a world where design meets technology, where Vuforia's\
                augmented reality wizardry breathes life into air conditioner data.\
                AuraFlow is on a mission to captivate users with an interactive journey\
                into real-time performance metrics. Through Unity3D and Vuforia, we're\
                about to show you how creativity and technology dance together in the\
                world of air conditioning."], className='guide')
    elif name == 'Introduction':
        return html.P([
                "Prepare to be wowed! AuraFlow is your ticket to a revolutionized way\
                of understanding air conditioner data, thanks to the enchantment of\
                augmented reality."], className='guide')
    elif name == 'Objectives':
        return html.P([
                "We're not just here to impress. We're on a mission to elevate your grasp of air\
                conditioner performance, dazzle you with the power of augmented reality,\
                and redefine creative design."], className='guide')
    elif name == 'Expected Results':
        return html.P([
                "Hold onto your seats! AuraFlow is set to deliver an AR application that doesn't just show you data,\
                but invites you to dance with it. It's intuitive, it's captivating, and it's going to change the way\
                you see air conditioning performance."], className='guide')
    else:
        return html.P([
                "Ever wondered what happens when technology meets pure magic? That's the story of Augmented Reality\
                (AR), a game-changer in industries across the board. We're talking about an experience that overlays\
                digital marvels onto your real world. And when it comes to air conditioning systems, AR isn't just a\
                tool - it's a revolution. Say goodbye to dull charts and graphs; we're bringing performance metrics\
                to life, right before your eyes. Get ready to step into a world where data isn't just understood,\
                it's felt. Welcome to AuraFlow!"], className='guide')


def create_card_for_selection():
    select_room = dbc.Card(
        [
            html.Div(
                dbc.CardBody([
                    dbc.Row(html.H5('Select Room')),
                    dbc.Row(
                        dcc.Dropdown(options=['NTUT - LIBRARY', 'NTUT - ROOM 424'],
                        value='NTUT - LIBRARY',
                        placeholder='Choose lag',
                        persistence=True,
                        persistence_type='session',
                        id='d2-dropdown',
                        style={'font-size': '18px'})),
                ]),
                className='my-button'
            ),
        ], 
        style={"border": "none"},
        inverse=True,
    )
    return select_room

def create_feature_for_selection(options):
    select_feature = dbc.Card(
        [
            html.Div(
                dbc.CardBody([
                    dbc.Row(html.H5('Select Feature')),
                    dbc.Row(
                        dcc.Dropdown(options=options,
                        value=options[0],
                        # placeholder='Choose lag',
                        persistence=True,
                        persistence_type='session',
                        id='feature_dropdown',
                        style={'font-size': '18px'})),
                ]),
                className='my-button'
            ),
        ], 
        style={"border": "none"},
        inverse=True,
    )
    return select_feature

def create_feature_for_prediction():
    select_feature = dbc.Card(
        [
            html.Div(
                dbc.CardBody([
                    dbc.Row(html.H5('Select Feature to Forecast')),
                    dbc.Row(
                        dcc.Dropdown(options=['Temperature', 'Humidity', 'CO2'],
                        value='Temperature',
                        # placeholder='Choose lag',
                        persistence=True,
                        persistence_type='session',
                        id='feature_prediction',
                        style={'font-size': '18px'})),
                ]),
                className='my-button'
            ),
        ], 
        style={"border": "none"},
        inverse=True,
    )
    return select_feature