from .pairs import pairs

def pair_select():
    try:
        pair = int(input("\n--Select a pair--\n[1] EUR/USD\n[2] USD/JPY\n[3] GBP/USD\n"))
        try:
            pair = pairs[pair]
            return pair
        except KeyError:
            print("\nPlease select one of the provided options...")
            return (pair_select())
        except Exception as e:
            print("\n", type(e).__name__)
            return (pair_select())
    except ValueError:
        print("\nPlease select one of the provided options...")
        return (pair_select())
    except KeyError:
        print("\nPlease select one of the provided options...")
        return(pair_select())
    except Exception as e:
        print("\n", type(e))
        return (pair_select())
