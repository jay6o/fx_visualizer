from ..env import *
def get_data(requests, json, pair, granularity, from_date, to_date):
  try:
    with requests.get(f"{DEMO_URL}/v3/accounts/{DEMO_ACC_ID}/instruments/{pair}/candles?granularity={granularity}&from={from_date}&to={to_date}", headers={"Authorization": f"Bearer {DEMO_API_KEY}"}, stream=True) as r:
            if r.status_code == 200:
                for line in r.iter_lines(decode_unicode=True):
                    with open("data.json", "w") as data_output:
                        data_output.write(line)
            else:
                print("HTTP error: line 4 of /modules/get_data.py")
                print(r)
  except Exception as e:
    print(e)
