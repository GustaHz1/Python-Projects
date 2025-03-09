from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import datetime
import time

driver = webdriver.Chrome()
driver.get("https://curso-web-scraping.pages.dev/#/desafio/1")
driver.fullscreen_window()

botao = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/button')
botao.click()


# Carregando os dados do arquivo json e salvando na variavel
with open('./desafio_1.json') as file:
    data = json.load(file)

for linha in range(len(data)):

    # Buscando os elementos no site e preenchendo 
    # Esperando até que o primeiro elemento do formulario esteja carregado, evitando erros na execução
    wait = WebDriverWait(driver, timeout=2) 
    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email.clear()
    email.send_keys(data[linha]['email'])
    senha = driver.find_element(By.NAME, 'senha')
    senha.clear()
    senha.send_keys(data[linha]['senha'])

    # Convertendo o dado em um tipo de data, passando o formato como parâmetro
    data_nasc = datetime.datetime.strptime(data[linha]['data-de-nascimento'], '%Y-%m-%d')

    # Separando cada checkbox em uma variavel e selecionando a checkbox pelo texto
    dia = Select(driver.find_element(By.NAME, 'dia'))
    dia.select_by_visible_text(str(data_nasc.day))
    mes = Select(driver.find_element(By.NAME, 'mes'))
    mes.select_by_visible_text(str(data_nasc.month))
    ano = Select(driver.find_element(By.NAME, 'ano')) 
    ano.select_by_visible_text(str(data_nasc.year))

    assinatura = driver.find_element(By.ID, 'airplane-mode')
    # Validando se o botão está atividade pelo atributo da página
    botao_assinatura = True if assinatura.get_attribute('aria-checked') == 'true' else False

    # Validando se o usuario deseja assinar ou não, caso o valor booleano esteja diferente do atributo da página, selecionamos o botão
    if botao_assinatura != data[linha] ['newsletter']:
        assinatura.click()

    enviar = driver.find_element(By.CSS_SELECTOR, 'form button[type="submit"]')
    enviar.click()
    
    wait = WebDriverWait(driver, timeout=2) 
    
    time.sleep(3)