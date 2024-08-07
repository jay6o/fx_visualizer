from .pair_select import pair_select
from .granularity_select import granularity_select
from .timerange_select import timerange_select
from ..helpers.calculate_daterange import calculate_daterange

def menu():
    pair = pair_select()
    granularity = granularity_select()
    timerange = timerange_select(granularity=granularity)
    dates = calculate_daterange(timerange)
    print(f"\n--Visualizing data for {pair}--\nData: {timerange}\nGranularity: {granularity}")
    return [pair, granularity, dates[0], dates[1]]
