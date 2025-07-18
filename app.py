import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Load your data
df = pd.read_csv('element_family_summary.csv')

# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Interactive Element-Family Concentration Visualization"),
    dcc.Dropdown(
        id='element-dropdown',
        options=[{'label': elem, 'value': elem} for elem in sorted(df['Element'].unique())],
        value='Ag',  # Initial element
        clearable=False
    ),
    dcc.Graph(id='sunburst-chart', style={'height':'80vh'})
])

# Callback to update graph based on selected element
@app.callback(
    Output('sunburst-chart', 'figure'),
    Input('element-dropdown', 'value')
)
def update_graph(selected_element):
    filtered_df = df[df['Element'] == selected_element]

    fig = px.sunburst(
        filtered_df,
        path=['Element', 'Family'],
        values='Total_Concentration',
        color='Total_Concentration',
        color_continuous_scale='Viridis',
        title=f'Total Concentration of {selected_element} by Plant Family'
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
