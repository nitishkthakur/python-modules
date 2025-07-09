import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout with blue navbar
app.layout = html.Div([
    # Blue Navbar
    dbc.NavbarSimple(
        brand="App 1",
        brand_href="#",
        color="primary",
        dark=True,
        style={"marginBottom": "20px"}
    ),
    
    # Main content
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H3("Chat Application 1", className="mb-3"),
                
                # Chat window
                html.Div(
                    id="chat-window-1",
                    style={
                        "height": "300px",
                        "border": "1px solid #ccc",
                        "padding": "10px",
                        "marginBottom": "10px",
                        "overflowY": "scroll",
                        "backgroundColor": "#f8f9fa"
                    }
                ),
                
                # Input section
                dbc.Row([
                    dbc.Col([
                        dbc.Input(
                            id="text-input-1",
                            placeholder="Type your message...",
                            type="text"
                        )
                    ], width=9),
                    dbc.Col([
                        dbc.Button("Send", id="send-button-1", color="primary", className="w-100")
                    ], width=3)
                ])
            ])
        ])
    ])
])

# Callback for chat functionality
@app.callback(
    Output("chat-window-1", "children"),
    Input("send-button-1", "n_clicks"),
    State("text-input-1", "value"),
    State("chat-window-1", "children")
)
def update_chat(n_clicks, message, current_chat):
    if n_clicks and message:
        if current_chat is None:
            current_chat = []
        new_message = html.Div([
            html.Strong("You: "),
            message
        ], style={"marginBottom": "5px"})
        current_chat.append(new_message)
        return current_chat
    return current_chat or []

if __name__ == "__main__":
    app.run(debug=True, port=8051)
