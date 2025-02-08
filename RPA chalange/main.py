import pandas as pd
import pyautogui
import selenium
from pyautogui import click, press, write
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Lendo o Dataframe
tabela = pd.read_excel('challenge.xlsx')

# Abrindo o navegador
driver = webdriver.Chrome()
driver.get('https://rpachallenge.com')
driver.fullscreen_window()

# Clicando no botão de iniciar
driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()

for linha in tabela.index:
    
    # Variavel recebendo o valor da linha do DataFrame
    primeiro_nome = tabela.loc[linha, "First Name"]
    # Buscando a tag input e se contém o texto no campo especifico
    primeiro_nome_campo = driver.find_element(By.XPATH, "//input[@ng-reflect-name = 'labelFirstName']")
    # Enviando as informações
    primeiro_nome_campo.send_keys(primeiro_nome)
   #primeiro_nome_campo.send_keys(Keys.ENTER)
    
    # Variavel recebendo o valor da linha do DataFrame
    ultimo_nome = tabela.loc[linha, "Last Name "]
    # Buscando a tag input e se contém o texto no campo especifico
    ultimo_nome_campo = driver.find_element(By.XPATH, "//input[@ng-reflect-name = 'labelLastName']")
    # Enviando as informações
    ultimo_nome_campo.send_keys(ultimo_nome)
    #ultimo_nome_campo.send_keys(Keys.ENTER)
    
    # Variavel recebendo o valor da linha do DataFrame
    empresa = tabela.loc[linha, "Company Name"]
    
    try:
    
        # Buscando a tag input e se contém o texto no campo especifico
        empresa_campo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name = 'labelCompanyName']"))
        )
     
        empresa_campo.send_keys(empresa)
        #empresa_campo.send_keys(Keys.ENTER)
    
    except Exception as e:
        print(f"Campo não encontrado! {e}")
    
    # Variavel recebendo o valor da linha do DataFrame
    funcao = tabela.loc[linha, "Role in Company"]
    # Buscando a tag input e se contém o texto no campo especifico
    funcao_campo = driver.find_element(By.XPATH, "//input[@ng-reflect-name = 'labelRole']")
    # Enviando as informações
    funcao_campo.send_keys(funcao)
    #funcao_campo.send_keys(Keys.ENTER)
    
    # Variavel recebendo o valor da linha do DataFrame
    endereco = tabela.loc[linha, "Address"]
    # Buscando a tag input e se contém o texto no campo especifico
    endereco_campo = driver.find_element(By.XPATH, "//input[@ng-reflect-name = 'labelAddress']")
    # Enviando as informações
    endereco_campo.send_keys(endereco)
    #endereco_campo.send_keys(Keys.ENTER)
    
    # Variavel recebendo o valor da linha do DataFrame
    email = tabela.loc[linha, "Email"]
    # Buscando a tag input e se contém o texto no campo especifico
    email_campo = driver.find_element(By.XPATH, "//input[@ng-reflect-name = 'labelEmail']")
    # Enviando as informações
    email_campo.send_keys(email)
    #email_campo.send_keys(Keys.ENTER)
    
    # Variavel recebendo o valor da linha do DataFrame
    numero = tabela.loc[linha, "Phone Number"]
    # Buscando a tag input e se contém o texto no campo especifico
    numero_campo = driver.find_element(By.XPATH, "//input[@ng-reflect-name = 'labelPhone']")
    # Enviando as informações
    numero_campo.send_keys(str(numero))
    #numero_campo.send_keys(Keys.ENTER)
    
    driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()