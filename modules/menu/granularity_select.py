def granularity_select():
    try:
        granularity = int(input("\n\n--Select a granularity--\n[1] 5 Seconds\n[2] 30 Seconds\n[3] 1 Minute\n[4] 5 Minute\n[5] 15 Minute\n[6] 30 Minute\n[7] 1 Hour\n[8] 4 Hour\n[9] 6 Hour\n[10] 12 Hour\n[11] Daily\n[12] Weekly\n[13] Monthly\n"))
        options = {1: "S5",
                    2: "S30",
                    3: "M1",
                    4: "M5",
                    5: "M15",
                    6: "M30",
                    7: "H1",
                    8: "H4",
                    9: "H6",
                    10: "H12",
                    11: "D",
                    12: "W",
                    13: "M"}
        try:
            granularity = options[granularity]
            return granularity
        except KeyError:
            print("\n\nPlease select one of the options provided...")
            return(granularity_select())
        except Exception as e:
            print("\n\n", type(e).__name__)
            return (granularity_select())
            return 
    except ValueError:
        print("\n\nPlease select one of the options provided...")
        return(granularity_select())
