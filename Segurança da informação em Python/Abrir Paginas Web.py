import webbrowser
from tkinter import *

# Inicializador da biblioteca Tkinter
root = Tk()

# Definindo o título da página e o tamanho
root.title("Abrir Browser")
root.geometry("300x200")

# Função que define a página web a ser aberta
def google():
    webbrowser.open("www.google.com")

# Botão para abrir a página
my_google = Button(root, text = 'Abrir o Google', command = google).pack(pady = 20)

root.mainloop()