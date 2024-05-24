import requests

URL = 'https://httpbin.dev/get'

params = {
    'name': 'Matias Aless',
    'password': '123',
    'email': 'mati@codigofacilito.com'
}

response = requests.get(URL, params=params) # se manda la query atravez del diccionario params, para información sensible, como la usamos POST 

if response.status_code == 200:
    payload = response.json()
    params = payload['args']
    
    print(params['name'])
    print(params['password'])
    print(params['email'])
    
    
    print(response.url)