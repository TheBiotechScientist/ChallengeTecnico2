# F. Javier Morales M.
# 26/04/2023
# Windows 10 Pro x64 21H2
# conda 4.11.0
# Python 3.11.3
# Atom Editor 1.55.0
# Docker Desktop 4.18.0
# git version 2.30.1.windows.1


from bs4 import BeautifulSoup as bs
import requests
import json

url = input('Visita la página \n https://super.walmart.com.mx/all-departments \n y selecciona el link de una categoría de algún departamento. Copia el link y pegao a continuación: \n')
ind = url.index('x')
main_url = url[:ind+1]

# Agregamos la información adicional de headers para obtener acceso al sitio
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}

# Hacemos la petición
response = requests.get(url, headers=header)

# Obtenemos el contenido html
soup = bs(response.text, 'html.parser')

# Se identificaron los elementos y clases que contienen la información pertinente
url_h3s = soup.find_all('a', {'class': r'absolute w-100 h-100 z-1 hide-sibling-opacity'})

# Separamos titulos h3 de los urls
h3s = [h.text for h in url_h3s]
urls = [u.get('href') for u in url_h3s]

# Localizamos los precios
prices = [p.text for p in soup.find_all('div', {'class': 'mr1 mr2-xl b black lh-copy f5 f4-l'})]

# Diccionario para almacenar la información
result = dict()

# Vaciamos los datos en el diccionario
for h3,price,url in zip(h3s,prices,urls):
    result[h3] = {'Precio' : price, 'Url' : main_url+url}


print(result)

# Generación de archivo JSON
with open('challenge-2.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
