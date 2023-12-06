import pandas as pd

def getCardsData(df):
    df['date'] = pd.to_datetime(df['date'])
    cards_df = df.loc[df['state'] == 'TOTAL']
    return cards_df

def createCard(df):
    card_df = getCardsData(df)
    return card_df.iloc[-1]