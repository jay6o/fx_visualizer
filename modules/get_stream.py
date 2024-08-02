from env import DEMO_API_KEY, DEMO_ACC_ID, DEMO_STREAM_URL

def get_stream(requests, json):
    try:
        with requests.get(f"{DEMO_STREAM_URL}/v3/accounts/{DEMO_ACC_ID}/pricing/stream?instruments=GBP_JPY", 
                          headers={"authorization": f"Bearer {DEMO_API_KEY}"}, stream=True) as r:
            if r.status_code == 200:
                for line in r.iter_lines():
                    line = json.loads(line)
                    print(line)

    except Exception as e:
        print(e)