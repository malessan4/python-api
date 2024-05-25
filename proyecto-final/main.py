import requests
from settings import *

code = 'fb91db9f26af0fabbe16'

URL = 'https://github.com/login/oauth/access_token'

params = {
    'client_id' : CLIENT_ID,
    'client_secret' : SECRET_ID,
    'code' : code
}

headers = {
    'Accept' : 'application/json'
}

response = requests.post(URL, params=params, headers=headers)

if response.status_code == 200:
    print(response.json())