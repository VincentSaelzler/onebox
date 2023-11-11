import requests
import json

BASE_URL = "https://api.godaddy.com"

# these are just for testing
API_KEY = "dKst8pghnmJ4_Wh8njbkCKACzqVScuyUDvE"
API_SECRET = "UUjLvyCJU8tdp84sV4kMNf"

endpoint = "/v1/domains"

headers = {
    'Authorization': f'sso-key {API_KEY}:{API_SECRET}',
    'Content-Type': 'application/json'
}

r = requests.get(f'{BASE_URL}{endpoint}/hearty.cooking/records',headers=headers)

records = json.loads(r.text)
root_host_records = [record for record in records if record['type'] == 'A' and record['name'] == '@']

if len(root_host_records) != 1:
    raise IndexError('expecting exactly one host record for the domain root')

root_host_record = root_host_records[0]

print(json.dumps(o, indent=2))


