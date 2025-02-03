import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import ttk
import customtkinter as ctk

ctk.set_appearance_mode("dark")

# Criando a janela principal
janela = ctk.CTk()
janela.title("Automação de Tarefas")
janela.geometry("300x350") 

# Criando um campo de entrada
Label(janela, text="Digite sua pesquisa:", bg="#555", fg="white", borderwidth=3, relief="ridge", ).pack(pady=5)
entrada = Entry(janela, width=30, bg="#555", fg="white", borderwidth=3, relief="ridge")
entrada.pack(pady=5)

# Melhorando a parte visual da janela
style = ttk.Style()
style.theme_use("clam")
# Cor preta
janela.configure(bg="#2E2E2E")

def google():
    pesquisa = entrada.get() 

    pyautogui.PAUSE = 1

    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")


    time.sleep(3)
    
    pyautogui.click(x=438, y=370)
    pyautogui.write(pesquisa)
    pyautogui.press("enter")

def youtube():
    pesquisa_youtube = entrada.get() 
    
    driver = webdriver.Chrome()

    driver.get('https://www.youtube.com')
    
    
    time.sleep(3)
    
    resultado_youtube = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
    resultado_youtube.send_keys(pesquisa_youtube)
    resultado_youtube.send_keys(Keys.RETURN)  
    
    driver.fullscreen_window()

def chatgpt():
    pesquisa_chat = entrada.get() 
    
    pyautogui.PAUSE = 1
    
    time.sleep(1)
    
    # Abrindo o Chrome
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    
    time.sleep(3)
    
    pyautogui.write('https://chat.openai.com')
    pyautogui.press("enter")
    
    time.sleep(3)
    
    pyautogui.write(pesquisa_chat)
    pyautogui.press("enter")

def github():
    driver = webdriver.Chrome()
    driver.get('https://github.com/GustaHz1')
    driver.fullscreen_window()

def spotify():
    pesquisar_musica = entrada.get()  
    
    pyautogui.PAUSE = 1
    
    pyautogui.press("win")
    pyautogui.write("spotify")
    pyautogui.press("enter")
    
    time.sleep(6)
    
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(2)
    pyautogui.write(pesquisar_musica)
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.press('enter')

    
    
   

# Criando botões para cada ação
Button(janela, text="Pesquisar no Google",bg="#555", fg="white", borderwidth=3, relief="ridge", command=google).pack(pady=10)
Button(janela, text="Pesquisar no Youtube",bg="#555", fg="white", borderwidth=3, relief="ridge", command=youtube).pack(pady=10)
Button(janela, text="Pesquisar no ChatGPT",bg="#555", fg="white", borderwidth=3, relief="ridge", command=chatgpt).pack(pady=10)
Button(janela, text="Abrir o GitHub",bg="#555", fg="white", borderwidth=3, relief="ridge", command=github).pack(pady=10)
Button(janela, text="Tocar Música no Spotify",bg="#555", fg="white", borderwidth=3, relief="ridge", command=spotify).pack(pady=10)

# Iniciando a interface gráfica
janela.mainloop()
