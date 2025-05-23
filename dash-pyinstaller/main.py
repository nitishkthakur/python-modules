import dash
from dash import dcc, html, Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    style={"maxWidth": 500, "margin": "60px auto", "padding": 20, "fontFamily": "sans-serif"},
    children=[
        html.H2("String Reverser"),
        dcc.Input(
            id='input-text',
            type='text',
            placeholder='Enter your text here...',
            style={"width": "100%", "padding": "8px", "marginBottom": "12px"}
        ),
        html.Button('Submit', id='submit-btn', n_clicks=0, style={"display": "block", "marginBottom": "12px"}),
        html.Div(id='output-reversed', style={"fontSize": 22, "color": "#333"})
    ]
)

@app.callback(
    Output('output-reversed', 'children'),
    Input('submit-btn', 'n_clicks'),
    State('input-text', 'value')
)
def reverse_string(n_clicks, value):
    if n_clicks and value:
        return f"Reversed: {value[::-1]}"
    return ""

if __name__ == '__main__':
    app.run(debug=True)
