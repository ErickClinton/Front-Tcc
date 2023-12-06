import pandas as pd
import pickle
from pmdarima.arima import auto_arima

train_set = pd.read_csv('data/covid/processed/time_series/new_deaths_train_set.csv')

train_set.set_index('date', inplace=True)
time_series = train_set['deaths']

model = auto_arima(
    time_series,
    start_p=1, 
    tart_q=1,
    max_p=3, 
    max_q=3, 
    m=12,              
    start_P=0, 
    d=1, 
    D=1, 
    trace=True,
    error_action='ignore',  
)

pickle.dump(model, open('models/new_deaths_predictor.sav', 'wb'))