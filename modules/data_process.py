#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
#%%
import json
import pandas as pd
import mplfinance as mpf

def preprocess(json, pandas, file):
    with open(file, 'r') as file:
        data = json.load(file)
        candles = data['candles']

    # Add JSON candle data to table
    df = pd.DataFrame(candles)

    # Convert time data to datetime
    df['time'] = pd.to_datetime(df['time'])

    # Extract OHLC 
    df['open'] = df['mid'].apply(lambda x: float(x['o']))
    df['high'] = df['mid'].apply(lambda x: float(x['h']))
    df['low'] = df['mid'].apply(lambda x: float(x['l']))
    df['close'] = df['mid'].apply(lambda x: float(x['c']))

    # Drop unneeded mid column
    df = df.drop('mid', axis=1)

    # Set index to datetime
    df.set_index('time', inplace=True)

    # Plot chart
    mpf.plot(df, type='candlestick', volume=True, title="GBPJPY Monthly Chart Since 2010")
    mpf.show()

if __name__ == "__main__":
    preprocess(json, pd, 'modules/gj_2010_2024_M.json')
# %%
