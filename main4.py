import os
import requests

URL = 'https://codigofacilito.com/images/cody' # png

# Crear directorio si no existe
if not os.path.exists('images'):
    os.makedirs('images')

response = requests.get(URL, stream=True) # petición

if response.status_code == 200:
    content_type = response.headers.get('Content-Type')
    if 'image' in content_type:
        with open('images/cody.png', 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print("Imagen guardada exitosamente.")
    else:
        print(f"El contenido recibido no es una imagen. Content-Type: {content_type}")
else:
    print(f"Error al descargar la imagen. Código de estado: {response.status_code}")