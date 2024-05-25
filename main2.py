import requests

URL = 'https://httpbin.dev/post'

# Query
# Cuerpo de peticion
# Encabezado

headers = {
    'course': 'Curso de Python',
    'version': '2.0',
    'author': 'Eduardo Ismael'
}

params = {
    'name'
}



response = requests.post(URL, headers=headers)

if response.status_code == 200:
    print(response.text)