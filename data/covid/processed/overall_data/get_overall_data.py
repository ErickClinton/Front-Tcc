import pandas as pd

df1 = pd.read_csv('data/covid/raw/cases-brazil-cities-time_2020.csv')
df2 = pd.read_csv('data/covid/raw/cases-brazil-cities-time_2021.csv')
df3 = pd.read_csv('data/covid/raw/cases-brazil-cities-time_2022.csv')
df4 = pd.read_csv('data/covid/raw/cases-brazil-cities-time_2023.csv')

df_concat = pd.concat([df1, df2, df3, df4], axis=0)

#epi_week,date,state,city,newDeaths,deaths,newCases,totalCases,deaths_per_100k_inhabitants,totalCases_per_100k_inhabitants,deaths_by_totalCases

df_concat.to_csv('data/processed/overall_data/overall_data.csv', index=False)