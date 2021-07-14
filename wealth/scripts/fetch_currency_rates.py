from urllib import request
import json

url = 'https://open.exchangerate-api.com/v6/latest/USD'

with request.urlopen(url) as resp:
    json_str = resp.read().decode('utf-8', errors='ignore')
    print(json_str)
    
    json_obj = json.loads(json_str)
    if 'success' == json_obj['result']:
        new_json_obj = {
            'result': json_obj['result'],
            'base_code': json_obj['base_code'],
            'next_update_time_interval': json_obj['time_next_update_unix'],
            'last_update_time_interval': json_obj['time_last_update_unix'],
            'rates': json_obj['rates'],
        }
        print(new_json_obj)
        
        new_json_str = json.dumps(new_json_obj)
        print(new_json_str)

        with open('rates.json', 'w') as file:
            file.write(new_json_str)
