from dash import html
import dash_bootstrap_components as dbc

_footer = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([html.Hr([], className = 'hr-footer')], width = 12)
        ]),
        dbc.Row([
	        # dbc.Col([], width = 1),
            dbc.Col(['Created by Steven Kuo, 2023, Inspired by Gabri-al (sarima_dashboard) & (dash-manufacture-spc-dashboard)'], width = 8),
            dbc.Col([], width =2),
	        dbc.Col([
                html.Ul([
                    html.Li([
                        html.A([ html.I(className="fa-brands fa-github me-3 fa-1x")], href='https://github.com/StevenKH15/aeroflow_uni_project'),
                        html.A([ html.I(className="fa-brands fa-linkedin me-3 fa-1x")], href='https://www.linkedin.com/in/steven-yen-ting-kuo/'),
                    ])
                ], className='list-unstyled d-flex justify-content-center justify-content-md-start')
            ], width = 2)
        ])
    ], fluid=True)
], className = 'footer')