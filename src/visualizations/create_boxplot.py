import pandas as pd

def getBoxPlotData(df):
    
    df['date'] = pd.to_datetime(df['date'])
    boxplot_df = df.loc[df['state'] == 'TOTAL']
    return boxplot_df

def createCasesBoxPlot(df):
    df = getBoxPlotData(df)
    df_cases_box = df.groupby(['epi_week'])['newCases'].sum().reset_index()
    df_cases_box = df_cases_box[['newCases', 'epi_week']].rename(columns={'newCases': 'count'})
    df_cases_box['type'] = 'Casos'
    return df_cases_box

def createDeathsBoxPlot(df):
    df = getBoxPlotData(df)
    df_deaths_box = df.groupby(['epi_week'])['newDeaths'].sum().reset_index()
    df_deaths_box = df_deaths_box[['newDeaths', 'epi_week']].rename(columns={'newDeaths': 'count'})
    df_deaths_box['type'] = 'Óbitos'
    return df_deaths_box

def creatVacBoxPlot(df):
    df = pd.read_csv('data/covid/processed/overall_data/vac.csv')
    df['type'] = 'Vacinados'
    return df