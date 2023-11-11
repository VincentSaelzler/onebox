import requests

BASE_URL = "https://api.godaddy.com"

# these are just for testing
API_KEY = "dKst8pghnmJ4_Wh8njbkCKACzqVScuyUDvE"
API_SECRET = "UUjLvyCJU8tdp84sV4kMNf"

endpoint = "/v1/domains"

headers = {
    'Authorization': f'sso-key {API_KEY}:{API_SECRET}',
    'Content-Type': 'application/json'
}

r = requests.get(f'{BASE_URL}{endpoint}/saelzler.com',headers=headers)

print('we made it!')


