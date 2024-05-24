import requests

URL = 'https://httpbin.dev/get?name=mati&password=123&email=mati@codigofacilito.com'
# query es todo la informacion que mandamos al servidor despues del signo ?

response = requests.get(URL) # GET

if response.status_code == 200:
    payload = response.json()
    params = payload['args']
    
    print(params['name'])
    print(params['password'])
    print(params['email'])
    