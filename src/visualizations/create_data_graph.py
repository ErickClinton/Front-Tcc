
import pandas as pd

def getGraphData(df):
    df['date'] = pd.to_datetime(df['date'])
    graph_df = df.loc[df['state'] == 'TOTAL']
    return graph_df

def createTotalDeathsGraph(df):
    graph_df = getGraphData(df)
    df_total_deaths= graph_df.loc[:, ['date', 'deaths']]
    df_total_deaths.set_index('date', inplace=True)
    df_total_deaths = df_total_deaths.resample('W').max()
    return df_total_deaths

def createTotalCasesGraph(df):
    graph_df = getGraphData(df)
    df_total_cases= graph_df.loc[:, ['date', 'totalCases']]
    df_total_cases.set_index('date', inplace=True)
    df_total_cases = df_total_cases.resample('W').max()
    return df_total_cases

