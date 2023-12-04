import pandas as pd

df = pd.read_csv('data/covid/processed/overall_data/overall_data.csv')
df['date'] = pd.to_datetime(df['date'])

data_BR = df.query("state != 'TOTAL'")[['epi_week', 'newCases', 'newDeaths', 'state', 'city']]

deaths_by_week = data_BR.groupby(['city', 'epi_week', 'state'])['newDeaths'].sum().reset_index()
deaths_by_week = deaths_by_week.groupby(['epi_week', 'state'])['newDeaths'].sum().reset_index()
deaths_by_week['cumulativeDeaths'] = deaths_by_week.groupby('state')['newDeaths'].cumsum()
deaths_by_week = deaths_by_week.groupby(['state'])['cumulativeDeaths'].max().reset_index()

cases_by_week = data_BR.groupby(['city', 'epi_week', 'state'])['newCases'].sum().reset_index()
cases_by_week = cases_by_week.groupby(['epi_week', 'state'])['newCases'].sum().reset_index()
cases_by_week['cumulativeCases'] = cases_by_week.groupby('state')['newCases'].cumsum()
cases_by_week = cases_by_week.groupby(['state'])['cumulativeCases'].max().reset_index()


deaths_by_week.to_csv('data/processed/geo_location/geo_location.csv', index=False)
cases_by_week.to_csv('data/processed/geo_location/geo_location_cases.csv', index=False)




