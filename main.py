import requests

URL = 'https://httpbin.dev/post'


data = { # lo use con el post
    'username': 'matias',
    'password': 'password123'
    
}
"""
params = { # lo use con el get
    'name': 'Matias Aless',
    'password': '123',
    'email': 'mati@codigofacilito.com'
}
"""
response = requests.post(URL, data=data) # se manda la query atravez del diccionario params, para información sensible, como la usamos POST 

if response.status_code == 200:
    payload = response.json()
# va con el get   params = payload['args']
    
    print(response.text)
    print(response.url)
    
"""    
    print(params['name'])
    print(params['password'])
    print(params['email'])
""" 
    
