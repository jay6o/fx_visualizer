from .pairs import pairs
from ..helpers.clear_out import clear_out

def pair_select(name, system):
    try:
        clear_out(name, system)
        pair = int(input("--Select a pair--\n[1] AUD/CAD\n[2] AUD/USD\n[3] EUR/CAD\n[4] EUR/GBP\n[5] EUR/JPY\n[6] EUR/USD\n[7] GBP/CAD\n[8] GBP/JPY\n[9] GBP/USD\n[10] USD/CAD\n[11] USD/CNH\n[12] USD/JPY\n"))
        try:
            pair = pairs[pair]
            return pair
        except KeyError:
            return (pair_select(name, system))
        except Exception as e:
            return (pair_select(name, system))
    except ValueError:
        return (pair_select(name, system))
    except KeyError:
        return(pair_select(name, system))
    except Exception as e:
        print("\n", type(e))
        return (pair_select(name, system))
