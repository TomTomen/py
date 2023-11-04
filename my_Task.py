from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
    dcc.Graph(id='top-population', figure = px.bar(df.groupby('country').sum()[['pop']].sort_values('pop', ascending = False)[:15])),
    dcc.Graph(id='pie-pop', figure = px.pie(values = df.groupby('continent').sum()['pop'].values,names = df.groupby('continent').sum()['pop'].index.tolist())),
    dcc.RangeSlider(id='year-slider',marks={str(year): str(year) for year in df['year']},  # Метки для ползунка
        min=df['year'].min(),
        max=df['year'].max(),
        step=1,  # Шаг для ползунка
        value=[1978, 2018]  # Значения по умолчанию
    )
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value'),
    Input('year-slider', 'value')

)
def update_graph(selected_country, selected_years):
    dff = df[df.country==selected_country]
    dff = dff[(dff['year'] >= selected_years[0]) & (dff['year'] <= selected_years[1])]

    return px.line(dff, x='year', y='pop')
    
#@callback(
#    Output('top-population', 'figure'),
#    [Input('year-slider', 'value')]
#)
#def update_figure(selected_years):
#    filtered_df = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]
#    fig = px.line(filtered_df, x='year', y='Value')
#    fig.update_layout(xaxis_tickangle=90)
#    return fig

if __name__ == '__main__':
    app.run(debug=True)
