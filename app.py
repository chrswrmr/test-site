import dash
import dash_html_components as html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Awesome Backtester!")
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)