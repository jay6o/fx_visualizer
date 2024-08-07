#%%
def preprocess(json, pd, file):
    with open(file, 'r') as file:
        data = json.load(file)
        candles = data['candles']

    # Add JSON candle data to table
    try:
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

        # Return the processed DataFrame
        return df
    except Exception as e:
        print(type(e).__name__, "\nProgram failed unexpectedly...")
#%%
