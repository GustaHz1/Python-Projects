import random, string

def validar_email(email):
    return email.endswith('@gmail.com') and " " not in email

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def analisar_dados(lista):
    media = sum(lista) / len(lista)
    desvio = (sum((x - media)**2 for x in lista) / len(lista))**0.5
    return {"média": media, "máximo": max(lista), "desvio": desvio}


temp = 10
lista = [1,2,3,4,5]
print(f"Lista: {analisar_dados(lista)}")
print(f"Senha: {gerar_senha()}")
print(f"Graus: {celsius_para_fahrenheit(temp)}")
print(f"Email: {validar_email("aoba@gmail.com")}")

