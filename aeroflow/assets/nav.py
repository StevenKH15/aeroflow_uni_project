import os
import dash
import base64
from dash import html
import dash_bootstrap_components as dbc


LOGO = os.path.join(os.getcwd(), "images/logo.png")
test_base64 = base64.b64encode(open(LOGO, 'rb').read()).decode('ascii')

_nav = dbc.Container([
    dbc.Row(html.Br()),
	dbc.Row([
        dbc.Col([], width=1),
        dbc.Col([
            # html.I(className="fa-solid fa-chart-simple fa-2x"),
            html.Img(src='data:image/png;base64,{}'.format(test_base64), height="100px", width="100px", style={'opacity':1, 'align':'center'}),
        ]),
	]),
    dbc.Row(html.Br()),
	dbc.Row([
        dbc.Nav(
	        [dbc.NavLink(page["name"], active='exact', href=page["path"]) for page in dash.page_registry.values()],
	        vertical=True, pills=True, class_name='my-nav')
    ])
])