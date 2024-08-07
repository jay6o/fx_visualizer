from .pair_select import pair_select
from .granularity_select import granularity_select
from .timerange_select import timerange_select
from ..helpers.calculate_daterange import calculate_daterange

def menu():
    pair = pair_select()
    granularity = granularity_select()
    timerange = timerange_select(granularity=granularity)
    dates = calculate_daterange(timerange)
    from_date = dates[0]
    to_date = dates[1]
    print(f"Visualizing data for {pair} from {from_date} to {to_date} with {granularity} granularity")
    return [pair, granularity, from_date, to_date]
