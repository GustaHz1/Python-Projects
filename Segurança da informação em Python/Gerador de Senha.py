import random
import string

#Lista de senhas criadas
senhas = []

while True:
    # Define o tamanho da senha
    tamanho = int(input("Qual o tamanho da senha que deseja: ")) 
    # Variável que define nossos caracteres para inseir na senha
    caracteres = string.ascii_letters + string.digits + "!@#$%&*_-+=/:;.,"
    # Gera números aleatórios
    aleatorio = random.SystemRandom() 

    # Gera um caracter aleatório, respeitando a quantidade estipulada pela variavel tamanho
    senha = ("".join(aleatorio.choice(caracteres) for i in range(tamanho)))
    print(senha, "\n")
    senhas.append(senha)
    print(senhas, "\n")

    escolha = input("Deseja inserir uma nova senha: ")
    if escolha == 'nao':
        break
    else:
        continue
    