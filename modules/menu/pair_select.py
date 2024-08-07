def pair_select():
    try:
        pair = int(input("--Select a pair--\n[1] EUR/USD\n[2] USD/JPY\n[3] GBP/USD\n"))
        options = {1: "EUR_USD",
                    2: "USD_JPY",
                    3: "GBP_USD"}
        try:
            pair = options[pair]
            return pair
        except KeyError:
            print("\n\nPlease select one of the provided options...")
            return (pair_select())
        except Exception as e:
            print("\n\n", type(e).__name__)
            return (pair_select())
    except ValueError:
        print("\n\nPlease select one of the provided options...")
        return (pair_select())
    except KeyError:
        print("\n\nPlease select one of the provided options...")
        return(pair_select())
    except Exception as e:
        print("\n\n", type(e))
        return (pair_select())
