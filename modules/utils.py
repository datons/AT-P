import requests
import pandas as pd

def get_data_stock_daily(symbol='AAPL', start='2023-01-01'):

    url_base = 'https://data.alpaca.markets/v2/stocks/bars'

    params = {
        'symbols': symbol,
        'start': start,
        'timeframe': '1Day',
    }

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": "PKG7Q4DBNED5BANQFM8U",
        "APCA-API-SECRET-KEY": "ZUcbfnk3MSYrU4PXjCrCRi8uXxd0lhKouSIMTOdZ"
    }

    response = requests.get(url_base, params=params, headers=headers)
    data = response.json()
    
    return data


def get_data_crypto_daily(symbol='BTC/USD', start='2023-01-01'):

    url_base = "https://data.alpaca.markets/v1beta3/crypto/us/bars"

    params = {
        'symbols': symbol,
        'start': start,
        'timeframe': '1Day',
    }
    
    headers = {"accept": "application/json"}
    
    response = requests.get(url_base, params=params, headers=headers)
    data = response.json()
    
    return data


def process_df(data, symbol):

    df = pd.DataFrame(data['bars'][symbol])
    df = (df
        .rename({
            'c': 'Close',
            'o': 'Open',
            'h': 'High',
            'l': 'Low',
            'v': 'Volume',
            't': 'Date'
            }, axis=1)
        .loc[:, ['Date','Open', 'High', 'Low', 'Close', 'Volume']]
        .assign(Date=lambda x: pd.to_datetime(x['Date']))
        .set_index('Date'))
    
    return df