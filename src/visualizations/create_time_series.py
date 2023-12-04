import pickle
import pandas as pd

def createDeathsTimeSeries():
    model = pickle.load(open('models/covid/time_series/new_deaths_predictor.sav', 'rb'))
    deaths_prediction = model.predict(n_periods=240)
    deaths_prediction = pd.DataFrame(deaths_prediction)
    deaths_prediction = deaths_prediction.resample('W').max()   
    return deaths_prediction

def createCasesTimeSeries():
    model = pickle.load(open('models/covid/time_series/new_cases_predictor.sav', 'rb'))
    cases_prediction = model.predict(n_periods=240)
    cases_prediction = pd.DataFrame(cases_prediction)
    cases_prediction = cases_prediction.resample('W').max()
    return cases_prediction