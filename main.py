#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3

#%%
import requests, json, pandas, mplfinance
from modules.menu.menu import menu
from modules.helpers.get_data import get_data
from modules.helpers.preprocess import preprocess
from modules.helpers.visualize import visualize

if __name__ == "__main__":
    information = menu()
    pair = information[0]
    granularity = information[1]
    get_data(requests, json, information[0], information[1], information[2], information[3])
    df = preprocess(json, pandas, "data.json")
    visualize(df, mplfinance, pair, granularity)
#%%
