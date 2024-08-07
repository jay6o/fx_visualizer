import datetime
from .get_daterange_string import get_daterange_string

def calculate_daterange(timerange):
    match timerange:
        case "M1":
            dates = get_daterange_string(datetime, minutes=1)
            return dates
        case "M5":
            dates = get_daterange_string(datetime, minutes=5)
            return dates
        case "M10":
            dates = get_daterange_string(datetime, minutes=10)
            return dates
        case "M15":
            dates = get_daterange_string(datetime, minutes=15)
            return dates
        case "M30":
            dates = get_daterange_string(datetime, minutes=30)
            print(dates)
            return dates
        case "1H":
            dates = get_daterange_string(datetime, hours=1)
            return dates
        case "2H":
            dates = get_daterange_string(datetime, hours=2)
            return dates
        case "4H":
            dates = get_daterange_string(datetime, hours=4)
            return dates
        case "6H":
            dates = get_daterange_string(datetime, hours=6)
            return dates
        case "8H":
            dates = get_daterange_string(datetime, hours=8)
            return dates
        case "12H":
            dates = get_daterange_string(datetime, hours=12)
            return dates
        case "1D":
            dates = get_daterange_string(datetime, days=1)
            return dates
        case "2D":
            dates = get_daterange_string(datetime, days=2)
            return dates
        case "3D":
            dates = get_daterange_string(datetime, days=3)
            return dates
        case "5D":
            dates = get_daterange_string(datetime, days=5)
            return dates
        case "1W":
            dates = get_daterange_string(datetime, weeks=1)
            return dates
        case "2W":
            dates = get_daterange_string(datetime, weeks=2)
            return dates
        case "1M":
            dates = get_daterange_string(datetime, weeks=4)
            return dates
        case "2M":
            dates = get_daterange_string(datetime, weeks=8)
            return dates
        case "4M":
            dates = get_daterange_string(datetime, weeks=16)
            return dates
        case "6M":
            dates = get_daterange_string(datetime, weeks=24)
            return dates
        case "1Y":
            dates = get_daterange_string(datetime, weeks=48)
            return dates
        case "5Y":
            dates = get_daterange_string(datetime, weeks=240)
            return dates
        case "10Y": # Does not return precise dates
            dates = get_daterange_string(datetime, weeks=480)
            return dates
