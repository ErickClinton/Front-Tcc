import pandas as pd

df = pd.read_csv('data/covid/processed/overall_data/overall_data.csv')
df['date'] = pd.to_datetime(df['date'])

data_new_BR = df.query("state == 'TOTAL'")[['epi_week', 'totalCases', 'deaths', 'date']]

train_set_size = int(1 * len(data_new_BR))


train_set = data_new_BR.iloc[:train_set_size, :]

new_deaths_train_set = train_set[['date', 'deaths']]
new_deaths_test_set = data_new_BR.iloc[train_set_size:, :]


new_cases_train_set = train_set[['date', 'totalCases']]
new_cases_test_set = data_new_BR.iloc[train_set_size:, :]


new_deaths_train_set.to_csv('data/processed/time_series/new_deaths_train_set.csv', index=False)
new_deaths_test_set.to_csv('data/processed/time_series/new_deaths_test_set.csv', index=False)

new_cases_train_set.to_csv('data/processed/time_series/new_cases_train_set.csv', index=False)
new_cases_test_set.to_csv('data/processed/time_series/new_cases_test_set.csv', index=False)

