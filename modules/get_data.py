from .env import *
def get_data(requests, json):
    try:
        with requests.get(f"{DEMO_URL}/v3/accounts/{DEMO_ACC_ID}/instruments/GBP_JPY/candles?granularity=M&from=2010-01-01 00:00:00&to=2024-07-01 00:00:00", headers={"Authorization": f"Bearer {DEMO_API_KEY}"}, stream=True) as r:
            if r.status_code == 200:
                for line in r.iter_lines(decode_unicode=True):
                    with open('gj_2010_2024_M.json', "w+") as data_output:
                        data_output.write(line)
            else:
                print("HTTP error: line 4 of /modules/get_data.py")
                print(r)
    except Exception as e:
        print(e)
