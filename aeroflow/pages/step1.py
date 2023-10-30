import dash
import warnings
import pandas as pd
import dash_daq as daq
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

warnings.filterwarnings("ignore")

dash.register_page(__name__, name='Dashboard', title='AuraFlow | Dashboard')

df = pd.read_csv('data/datatraining.txt')
df = df.rename(columns={'date':'Time'})
df['Time'] = pd.to_datetime(df['Time'], errors='raise')

params = list(df)
max_length = len(df)

suffix_row = '_row'
suffix_button_id = '_button'
suffix_sparkline_graph = '_sparkline_graph'
suffix_indicator = '_indicator'
suffix_current_value = '_current_value'

def generate_section_banner(title):
    return dbc.Row([dbc.Col(html.H1([title], className='row-titles'), width=11)])

def generate_metric_list_header():
    return generate_metric_row(
        "metric_header",
        {"height": "4rem", "textAlign": "center"},
        {"id": "m_header_1", "children": html.H4("Feature")},
        {"id": "m_header_3", "children": html.H4("Sparkline")},
        {"id": "m_header_4", "children": html.H4("Value")},
        {"id": "m_header_6", "children": html.H4("Status")},
    )

def generate_metric_row_helper(stopped_interval, index):
    item = params[index]

    div_id = item + suffix_row
    button_id = item + suffix_button_id
    sparkline_graph_id = item + suffix_sparkline_graph
    indicator_id = item + suffix_indicator
    current_value_id = item + suffix_current_value

    return generate_metric_row(
        div_id,
        None,
        {
            "id": item,
            "className": "metric-row-button-text",
            "children": html.H6(
                id=button_id,
                className="metric-row-button",
                children=item,
                title="Click to visualize live SPC chart",
            )
        },
        {
            "id": item + "_sparkline",
            "children": dcc.Graph(
                id=sparkline_graph_id,
                style={"width": "100%", "height": "95%"},
                config={
                    "staticPlot": False,
                    "editable": False,
                    "displayModeBar": False,
                },
                figure=go.Figure(
                    {
                        "data": [
                            {
                                "x": state_dict["Time"]["data"].tolist()[
                                    :stopped_interval
                                ],
                                "y": state_dict[item]["data"][stopped_interval-50:stopped_interval],
                                "mode": "lines+markers",
                                "name": item,
                                "line": {"color": "#3DED97"},
                            }
                        ],
                        "layout": {
                            "uirevision": True,
                            "margin": dict(l=0, r=0, t=4, b=4, pad=0),
                            "xaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,
                            ),
                            "yaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,
                            ),
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)",
                        },
                    }
                ),
            ),
        },
        {
            "id": current_value_id,
            "className": "metric-row-button-text",
            "children": html.H6(
                '{:.2f}'.format(state_dict[item]["data"][stopped_interval])
            )
        },
        {
            "id": item + "_pf",
            "children": daq.Indicator(
                id=indicator_id, value=True, color="yellow"
            ),
        },
    )


def generate_metric_row(id, style, col1, col2, col3, col6):
    if style is None:
        style = {"height": "4rem", "width": "100%"}

    return dbc.Col(
        id=id,
        className="row metric-row",
        style=style,
        children=[
            dbc.Col([], width=1),
            dbc.Col(
                id=col1["id"],
                className="one column",
                style={"margin-right": "2.5rem", "minWidth": "50px"},
                children=col1["children"],
                width=1
            ),
            dbc.Col(
                id=col2["id"],
                style={"height": "100%"},
                className="one column",
                children=col2["children"],
                width=6
            ),
            dbc.Col(
                id=col3["id"],
                style={"margin-right": "2.5rem", "minWidth": "50px"},
                className="four columns",
                children=col3["children"],
                width=1
            ),
            dbc.Col(
                id=col6["id"],
                style={"display": "flex", "justifyContent": "center", "align":"center"},
                className="one column",
                children=col6["children"],
                width=1
            ),
        ],
        width = 12,
    )

def build_top_panel(stopped_interval):
    return html.Div(
        id="top-section-container",
        className="row",
        children=[
            # Metrics summary
            html.Div(
                id="metric-summary-session",
                className="eight columns",
                children=[
                    generate_section_banner("Live data"),
                    html.Div(
                        id="metric-div",
                        children=[
                            generate_metric_list_header(),
                            html.Div(
                                id="metric-rows",
                                children=[
                                    generate_metric_row_helper(stopped_interval, 1),
                                    generate_metric_row_helper(stopped_interval, 2),
                                    generate_metric_row_helper(stopped_interval, 3),
                                    generate_metric_row_helper(stopped_interval, 4),
                                    generate_metric_row_helper(stopped_interval, 5),
                                    generate_metric_row_helper(stopped_interval, 6),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

def init_df():
    ret = {}
    for col in list(df[1:]):
        data = df[col]
        stats = data.describe()
        ret.update(
            {
                col: {
                    "count": stats["count"].tolist(),
                    "data": data,
                }
            }
        )

    return ret

state_dict = init_df()
layout = dbc.Container([
    html.Div(
        children=[
            build_top_panel(50),
            dcc.Interval(
                id="interval-component",
                interval=1 * 1000,  # in milliseconds
                n_intervals=50,  # start at batch 50
                disabled=False,
            ),
        ])
])
@callback(
    Output("metric-rows", "children"),
    Input("interval-component", "n_intervals"),
)
def print_interval(n_interval):
    return [
        generate_metric_row_helper(n_interval, 1),
        generate_metric_row_helper(n_interval, 2),
        generate_metric_row_helper(n_interval, 3),
        generate_metric_row_helper(n_interval, 4),
        generate_metric_row_helper(n_interval, 5),
        generate_metric_row_helper(n_interval, 6),
    ]