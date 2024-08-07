from .granularities import granularities

def granularity_select():
    try:
        granularity = int(input("\n--Select a granularity--\n[1] 5 Seconds\n[2] 30 Seconds\n[3] 1 Minute\n[4] 5 Minute\n[5] 15 Minute\n[6] 30 Minute\n[7] 1 Hour\n[8] 4 Hour\n[9] 6 Hour\n[10] 12 Hour\n[11] Daily\n[12] Weekly\n[13] Monthly\n"))
        try:
            granularity = granularities[granularity]
            return granularity
        except KeyError:
            print("\nPlease select one of the options provided...")
            return(granularity_select())
        except Exception as e:
            print("\n", type(e).__name__)
            return (granularity_select())
            return 
    except ValueError:
        print("\nPlease select one of the options provided...")
        return(granularity_select())
