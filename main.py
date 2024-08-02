#%%
import requests, json, pandas, mplfinance
from modules.get_data import get_data
from modules.preprocess import preprocess
from modules.visualize import visualize

if __name__ == "__main__":
    get_data(requests, json)
    df = preprocess(json, pandas, 'gj_2010_2024_M.json')
    visualize(df, mplfinance)
# %%
