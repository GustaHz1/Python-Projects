import pandas as pd
import pyautogui
import time
from pyautogui import click, press, write
from time import sleep

# Estipulando o intervalo para cada ação 
pyautogui.PAUSE = 0.5

# Abrindo o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Acessando o sistema
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Logando no sistema
pyautogui.click(x=514, y=372)
pyautogui.write("gustavo@gmail.com")
pyautogui.press("tab")
pyautogui.write("gustavohenrique12345")
pyautogui.press("tab")
pyautogui.press("enter")

# Lendo a base de dados com Pandas
tabela = pd.read_csv("produtos.csv", sep=";")
# Retorna as informações da tabela, retorna no terminal
print(tabela.info())
# Exclui as linhas vazias de uma coluna especifica 
tabela.dropna(subset=["obs"], inplace=True)

# Percorrendo as linhas da tabela 
for linhas in tabela.index:
    
    # Inserindo cada linha nos campos do formulario
    pyautogui.click(x=487, y=253)
    codigo = tabela.loc[linhas, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    marca = tabela.loc[linhas, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    tipo = tabela.loc[linhas, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    categoria = tabela.loc[linhas, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco = tabela.loc[linhas, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    
    custo = tabela.loc[linhas, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = tabela.loc[linhas, 'obs']
    pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(1000)
    

