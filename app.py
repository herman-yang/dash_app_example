#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type="text"),
    html.Div(id='my-div')
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):  # decorator
    return 'You\'ve entered. WOW!!! "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()

