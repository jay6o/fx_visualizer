def visualize(df, mplf, pair, granularity):
    try:
        mplf.plot(df, type="candlestick", volume=True, mav=(9, 20), title=f"{pair}, {granularity}")
        mplf.show()
    except Exception as e:
        print(type(e).__name__, "\nProgram failed unexpectedly...")
