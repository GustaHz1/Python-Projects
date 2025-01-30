import time
import pyautogui
from pyautogui import write, click, press
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def google():
    pesquisa = input("Pesquisa: ")

    pyautogui.PAUSE = 1

    # Abrindo o Chrome
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    # Aguardando 3 segundos para evitar erros
    time.sleep(3)

    # Selecionando a barra de pesquisa e inserindo a pesquisa desejada 
    pyautogui.click(x=438, y=370)
    pyautogui.write(pesquisa)
    pyautogui.press("enter")

def youtube():
    pesquisa_youtube = input("Pesquisa: ")
    
    # Abrindo o navegador 
    driver = webdriver.Chrome()
    
    # Abrindo o youtube 
    driver.get('https://www.youtube.com')
    
    # Esperando a página ser carregada
    time.sleep(3)
    
    resultado_youtube = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
    resultado_youtube.send_keys(pesquisa_youtube)
    # Pressiona o enter
    resultado_youtube.send_keys(Keys.RETURN)
    
    driver.fullscreen_window()

def chatgpt():
    pesquisa_chat = input("Pesquisa: ")
    
    pyautogui.PAUSE = 1
    
    time.sleep(1)
    
    # Abrindo o Chrome
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    
    time.sleep(3)
    
    pyautogui.write('https://chatgpt.com')
    pyautogui.press("enter")
    
    time.sleep(3)
    
    pyautogui.write(pesquisa_chat)
    pyautogui.press("enter")

def github():
    
    driver = webdriver.Chrome()
    
    driver.get('https://github.com/GustaHz1')
    
    driver.fullscreen_window()

def spotify():
    pesquisar_musica = input("Escolha a musica: ")
    
    pyautogui.PAUSE = 1
    
    pyautogui.press("win")
    pyautogui.write("spotify")
    pyautogui.press("enter")
    
    time.sleep(6)
    
    pyautogui.click(x=577, y=30)
    pyautogui.write(pesquisar_musica)
    pyautogui.press('enter')
    
    time.sleep(3)
    
    pyautogui.click(x=916, y=214)

while True:
    escolha = input("""
         [1]Pesquisar no Google
         [2]Pesquisar no Youtube
         [3]Pergunte ao ChatGPT
         [4]Entrar no GitHub
         [5]Abrir Spotify
         [6]Sair
         Escolha: """)
    
    if escolha == "1":
        google()
    elif escolha == "2":
        youtube()
    elif escolha == "3":
        chatgpt()
    elif escolha == "4":
        github()
    elif escolha == "5":
        spotify()
    elif escolha == "6":
        break
    else:
        print("Opção inválida!")
