from folium.plugins import HeatMap
import folium
import json
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import sys
sys.path.append('src/visualizations')
sys.path.append('src/utils')
from create_data_graph import createTotalCasesGraph, createTotalDeathsGraph
from create_cards import createCard
from create_time_series import createCasesTimeSeries, createDeathsTimeSeries
from create_boxplot import creatVacBoxPlot, createCasesBoxPlot, createDeathsBoxPlot
from create_bars import createStatesBar, createTotalNewCases, createTotalNewDeaths

df = pd.read_csv('data/covid/processed/overall_data/overall_data.csv')

# DATA_CARDS
df_card = createCard(df)
# BOX
df_deaths_box = createDeathsBoxPlot(df)
df_cases_box = createCasesBoxPlot(df)
df_vac_box = creatVacBoxPlot(df)
# BARS
df_death_bars = createTotalNewDeaths(df)
df_cases_bars = createTotalNewCases(df)
df_vac_bar = createStatesBar()
# DATA_GRAPH
df_all_time_deaths = createTotalDeathsGraph(df)
df_all_time_cases = createTotalCasesGraph(df)
# TIME_SERIES
total_deaths_prediction = createDeathsTimeSeries()
total_cases_prediction = createCasesTimeSeries()

# GEO_LOCATION
df_geo = pd.read_csv('data/covid/processed/geo_location/geo_location.csv')
df_geo_cases = pd.read_csv(
    'data/covid/processed/geo_location/geo_location_cases.csv')
with open('src/utils/brazil_geo.json') as f:
    brazil_geo = json.load(f)

df_heat = pd.read_csv('data/covid/processed/geo_location/cases-gps.csv')
heatmap = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
heat_data = [[row['lat'], row['lon'], row['total']]
             for index, row in df_heat.iterrows()]
HeatMap(heat_data).add_to(heatmap)
heatmap.save('heatmap.html')

app = Dash(__name__)

app.layout = html.Div(
    className="top",
    children=[
        html.H1('Monitoramento de Doenças - COVID Brasil'),

        html.Div(
            className='card-box',
            children=[
                html.Div(
                    className="data-card",
                    children=[
                        html.H4('Óbitos Acumulados'),
                        html.P(df_card['deaths']),
                        html.H4('Novos Óbitos'),
                        html.P(df_card['newDeaths'])
                    ]
                ),

                html.Div(
                    className="data-card",
                    children=[
                        html.H4('Casos Acumulados'),
                        html.P(df_card['totalCases']),
                        html.H4('Novos Casos'),
                        html.P(df_card['newCases'])
                    ]
                ),
            ]
        ),
        dcc.Graph(
            className='data-bar',
            figure=px.bar(
                df_death_bars,
                x="epi_week",
                y="newDeaths",
                template='plotly_dark',
                color='year',
                labels={'epi_week': 'Semana',
                        'newDeaths': 'Novos Óbitos', 'year': 'Ano'}
            )
        ),
        dcc.Graph(
            className='data-bar',
            figure=px.bar(
                df_cases_bars,
                x="epi_week",
                y="newCases",
                template='plotly_dark',
                color='year',
                labels={'epi_week': 'Semana',
                        'newCases': 'Novos Casos', 'year': 'Ano'}
            )
        ),
        html.Div(
            className='graph-series',
            children=[
                dcc.Graph(
                    className='data-graph',
                    figure=px.line(
                        df_all_time_deaths,
                        title='Óbitos Acumulados',
                        x=df_all_time_deaths.index,
                        y=df_all_time_deaths['deaths'],
                        template='plotly_dark',
                        labels={'date': 'Data', 'deaths': 'Óbitos'},
                        width = 750
                    )
                ),
                dcc.Graph(
                    className='time-series',
                    figure=px.line(
                        total_deaths_prediction,
                        title='Óbitos Acumulados (Previsão)',
                        x=total_deaths_prediction.index,
                        y=total_deaths_prediction[0],
                        range_y=[0, total_deaths_prediction[0].max()],
                        template='plotly_dark',
                        labels={'index': 'Data', '0': 'Óbitos'},
                        width = 750
                    )
                ),
            ]
        ),

        html.Div(
            className='graph-series',
            children=[
                dcc.Graph(
                    className='data-graph',
                    figure=px.line(
                        df_all_time_cases,
                        title='Casos Acumulados',
                        x=df_all_time_cases.index,
                        y=df_all_time_cases['totalCases'],
                        template='plotly_dark',
                        labels={'date': 'Data', 'totalCases': 'Casos'},
                        width = 750
                    )
                ),
                dcc.Graph(
                    className='time-series',
                    figure=px.line(
                        total_cases_prediction,
                        title='Casos Acumulados (Previsão)',
                        x=total_cases_prediction.index,
                        y=total_cases_prediction[0],
                        range_y=[0, total_cases_prediction[0].max()],
                        template='plotly_dark',
                        labels={'index': 'Data', '0': 'Casos'},
                        width = 750
                    )
                ),
            ]
        ),

        html.Div(
            children=[
                dcc.Graph(
                    id='box-plot-deaths',
                    className='box_plot',
                    figure=px.box(
                        df_deaths_box,
                        x="type", y="count",
                        template='plotly_dark',
                        labels={'type': 'Tipo de registro',
                                'count': 'Número de óbitos'},
                        width=500
                    )
                ),
                dcc.Graph(
                    id='box-plot-cases',
                    className='box_plot',
                    figure=px.box(
                        df_cases_box,
                        x="type", y="count",
                        template='plotly_dark',
                        labels={'type': 'Tipo de registro',
                                'count': 'Número de casos'},
                        width=500
                    )
                ),
                dcc.Graph(
                    id='box-plot-vac',
                    className='box_plot',
                    figure=px.box(
                        df_vac_box,
                        x="type", y="bp",
                        template='plotly_dark',
                        labels={'type': 'Tipo de registro',
                                'bp': 'Número de vacinados'},
                        width=500
                    )
                ),
            ],
            className='boxplot_box'
        ),
        dcc.Graph(
            className='data-bar',
            figure=px.bar(
                df_vac_bar, 
                x="st", 
                y=["case", "death", "vac"], 
                title="Casos, Óbitos e Vacinas (Terceira Dose) nos 5 Estados com Mais Casos",
                template='plotly_dark',
                labels={'case': 'Casos', 'vac': 'Vacinados', 'st': 'Estado', 'death': 'Óbitos'}
                )
        ),

        dcc.RadioItems(['Óbitos', 'Casos'], 'Óbitos',
                       inline=True, id='geo_radio', className='radio'),
        dcc.Graph(
            id='geo_graph',
            className='geo-map',
            figure=px.choropleth_mapbox(
                title='Total de Óbitos por Estado',
                height=700,
                template='plotly_dark',
                data_frame=df_geo,
                geojson=brazil_geo,
                locations='state',
                color='cumulativeDeaths',
                mapbox_style="carto-positron",
                center={"lat": -15.7801, "lon": -47.9292},
                zoom=2,
                range_color=(0, df_geo['cumulativeDeaths'].max()),
                labels={'cumulativeDeaths': 'Óbitos', 'state': 'Estado'},
            )
        ),
        html.H2('Total de Casos por Estado - Mapa de Calor'),

        html.Iframe(
            id='map',
            title='Total de Casos - Mapa de Calor',
            srcDoc=open('heatmap.html', 'r').read(),
            width='100%',
            height='600'
        ),
    ])


@app.callback(
    Output('geo_graph', 'figure'),
    Input('geo_radio', 'value')
)
def getGeoFigure(value):
    if (value == 'Óbitos'):
        fig = px.choropleth_mapbox(
            title='Total de Óbitos por Estado',
            height=700,
            template='plotly_dark',
            data_frame=df_geo,
            geojson=brazil_geo,
            locations='state',
            color='cumulativeDeaths',
            mapbox_style="carto-positron",
            center={"lat": -15.7801, "lon": -47.9292},
            zoom=2,
            range_color=(0, df_geo['cumulativeDeaths'].max()),
            labels={'cumulativeDeaths': 'Óbitos', 'state': 'Estado'},
        )
    else:
        fig = px.choropleth_mapbox(
            title='Total de Casos por Estado',
            height=700,
            template='plotly_dark',
            data_frame=df_geo_cases,
            geojson=brazil_geo,
            locations='state',
            color='cumulativeCases',
            color_continuous_scale="Viridis",
            mapbox_style="carto-positron",
            center={"lat": -15.7801, "lon": -47.9292},
            zoom=2,
            range_color=(0, df_geo_cases['cumulativeCases'].max()),
            labels={'cumulativeCases': 'Casos', 'state': 'Estado'},
        )
    return fig


if __name__ == '__main__':
    app.run_server()
