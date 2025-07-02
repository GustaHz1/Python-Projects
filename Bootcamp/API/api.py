import requests
from flask import Flask, jsonify

url = 'https://api.exchangerate-api.com/v4/latest/USD'
res = requests.get(url)

if res.ok:
    data = res.json()
    print(f"Cotação do real hoje: R${data['rates']['BRL']:.2f}")

