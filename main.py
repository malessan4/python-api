import requests

URL = 'https://httpbin.dev/get'

response = requests.get(URL) # GET
print(response)
print(response.status_code)
print(response.text) # string
print(response.json()) # al json lo usa como diccionario

payload = response.json()
print(payload.get('origin'))

print(response.url)