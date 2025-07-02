from datetime import datetime, date, timedelta

d = date(2025, 6 , 16)
print(d)

data = datetime(2025, 6, 16)
print(data)
print(datetime.today())

tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 40
tempo_grande = 50
data_atual = datetime.now()

# Usamos o timedelta para fazer calculos com datas
if tipo_carro == "P":
    data_estimada =  data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada =  data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada =  data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
    
