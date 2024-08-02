def visualize(df, mplf):
    mplf.plot(df, type="candlestick", volume=True, mav=(9, 20), title="GBP/JPY 14-Year Chart, Monthly")
    mplf.show()