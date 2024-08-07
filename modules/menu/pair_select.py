from .pairs import pairs
from ..helpers.clear_out import clear_out

def pair_select(name, system):
    try:
        clear_out(name, system)
        pair = int(input("--Select a pair--\n==MAJOR PAIRS==\n[1] AUD/CAD\n[2] AUD/JPY\n[3] AUD/USD\n[4] AUD/CHF\n[5] CAD/JPY\n[6] CHF/JPY\n[7] EUR/AUD\n[8] EUR/CAD\n[9] EUR/CHF\n[10] EUR/GBP\n[11] EUR/JPY\n[12] EUR/USD\n[13] GBP/AUD\n[14] GBP/CAD\n[15] GBP/CHF\n[16] GBP/JPY\n[17] GBP/USD\n[18] USD/CAD\n[19] USD/CHF\n[20] USD/CNH\n[21] USD/JPY\n==OTHER==\n[22] USD/CZK (Czech Krone)\n[23] USD/DKK (Danish Krone)\n[24] USD/HKD (Hong Kong Dollar)\n[25] USD/HUF (Hungarian Forint)\n[26] USD/MXN (Mexican Peso)\n[27] USD/NOK (Norwegian Krone)\n[28] USD/PLN (Polish Zloty)\n[29] USD/SEK (Swedish Krona)\n[30] USD/SGD (Singapore Dollar)\n[31] USD/THB (Thai Baht)\n[32] USD/TRY (Turkish Lira)\n[33] USD/ZAR (South African Rand)\n"))
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
