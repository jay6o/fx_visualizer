from .granularities import granularities
from ..helpers.clear_out import clear_out

def granularity_select(name, system):
    try:
        clear_out(name, system)
        granularity = int(input("--Select a granularity--\n[1] 5 Seconds\n[2] 30 Seconds\n[3] 1 Minute\n[4] 5 Minute\n[5] 15 Minute\n[6] 30 Minute\n[7] 1 Hour\n[8] 4 Hour\n[9] 6 Hour\n[10] 12 Hour\n[11] Daily\n[12] Weekly\n[13] Monthly\n"))
        try:
            granularity = granularities[granularity]
            return granularity
        except KeyError:
          return(granularity_select(name, system))
        except Exception as e:
          print("\n", type(e).__name__)
          return (granularity_select(name, system))
    except ValueError:
        return(granularity_select(name, system))
    except Exception as e:
        print(type(e))
        return(granularity_select(name, system))
