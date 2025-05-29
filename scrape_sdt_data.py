import requests
import time
import json

for i in range(1,38):
    time.sleep(1)
    response = requests.get(f"https://www.dreamteamfc.com/json/season/player_live_scores/{i}.json")
    data = response.json()

    with open(f'data/gw{i}_data.json', 'w') as f:
        json.dump(data, f)
    print(f'Saved GW{i}')