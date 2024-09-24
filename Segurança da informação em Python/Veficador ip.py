import json
from urllib.request import urlopen

# Definindo um url para ser trabalhada
url = 'https://ipinfo.io/json'

# 
respota = urlopen(url)

dados = json.load(respota)

ip = dados['ip']

print(f'detalhes ip: {ip}')
      