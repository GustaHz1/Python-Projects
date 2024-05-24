
#Forma de repetição sem FOR ou WHILE
a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1 
print(a)

#Exemplo de FOR que separa todas as vogais de uma palavra
#.UPPER é usado para colocar caracteres em maiusculo
texto = input("Informen um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ") #END é usado para adicionar caracter no final de um PRINT
else:
    print() #Quebra de linha 

#RANGE é usado para trabalhar com uma sequência de números
for numero in range(0, 101, 5):
    print(numero, end=" ")
print()

#Exemplo de WHILE, usado para continauar uma ação no seu código até que uma condição seja executada
opcao = -1
saldo= 1000
while opcao != 0:
    opcao = int(input("Selecione a opção que deseja: [1]-Sacar \n [2]-Depositar \n [3]-Saldo \n [0]-Sair  "))
    if opcao == 1:
        print("Saque realizado")
    elif opcao == 2:
        print("Deposito efetuado")
    elif opcao == 3:
        print(saldo)
    else:
        print("Processo finalizado")
print()

#Exemplo de CONTINUE, usado para pular determinado valor especificado no codigo
for numero in range (0,101):
    if numero % 4 == 0:
        print(numero, end=" ")
        continue
print()

#Exemplo de BREAK, usado para encerrar a execução do codigo
while - True:
    valor= int(input("Digite um numero: "))
    if valor % 2 == 0:
        break
print(valor)