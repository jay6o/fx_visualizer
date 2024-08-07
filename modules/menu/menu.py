from .pair_select import pair_select
from .granularity_select import granularity_select
from .timerange_select import timerange_select
from ..helpers.calculate_daterange import calculate_daterange
from ..helpers.clear_out import clear_out

def menu(name, system):
    pair = pair_select(name, system)
    granularity = granularity_select(name, system)
    timerange = timerange_select(name, system, granularity=granularity)
    dates = calculate_daterange(timerange)
    clear_out(name, system)
    print(f"--Visualizing data for {pair}--\nData: {timerange}\nGranularity: {granularity}")
    return [pair, granularity, dates[0], dates[1]]
