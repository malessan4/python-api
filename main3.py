import requests


# GET = get
# POST = post
# PUT = put
# DELETE = delete
"""
estas funciones van a retornar un objeto de tipo response. Permiten enviar valores
atravez de la query, el encabezado y la data.
"""

URL = 'https://httpbin.org/put'
response = requests.put(URL,
                        params={'name' : 'Eduardo'}, #query
                        headers={'version': '2.0'}, #headers
                        data={'id' : 1}) #cuerpo de la peticion

if response.status_code == 200:
    print(response.text)