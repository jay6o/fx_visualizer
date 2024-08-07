def visualize(df, mplf, pair, granularity):
    mplf.plot(df, type="candlestick", volume=True, mav=(9, 20), title=f"{pair}, {granularity}")
    mplf.show()
