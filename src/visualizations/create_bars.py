import pandas as pd
import sys
sys.path.append('src/utils')
from local_utils import adjust_epi_week 

def getBarsData(df):
    df['date'] = pd.to_datetime(df['date'])
    df_bars = df.loc[df['state'] == 'TOTAL']
    df_bars = df.loc[:, ['epi_week', 'newDeaths', 'newCases', 'date']]
    df_bars['year'] = df_bars['date'].dt.year
    df_bars.set_index('date', inplace=True)
    df_bars['epi_week'] = df_bars['epi_week'].apply(adjust_epi_week)
    df_bars['newDeaths'] = df_bars['newDeaths'] / 2
    df_bars['newCases'] = df_bars['newCases'] / 2
    return df_bars

def createTotalNewDeaths (df):
    bars_data = getBarsData(df)
    total_new_deaths = bars_data.groupby(['epi_week', 'year'])['newDeaths'].sum().reset_index()
    return total_new_deaths

def createTotalNewCases (df):
    bars_data = getBarsData(df)
    total_new_cases = bars_data.groupby(['epi_week', 'year'])['newCases'].sum().reset_index()
    return total_new_cases

def createStatesBar():
    df = pd.read_csv('data/covid/processed/overall_data/vac.csv')
    return df
