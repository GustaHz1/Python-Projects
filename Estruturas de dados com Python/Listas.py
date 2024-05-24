#LISTA com valores strings
frutas = ["Maça", "Laranja", "Melancia"]
#LISTA com apenas um valor string, o valor será separado letra por letra
letras = list("Python")
#LISTA vazia
vazio = []
#LISTA com metodo RANGE, a LISTA ira retornar uma sequencia numerica determinada por range
numeros = list(range(10))
#LISTA com valores diferentes, INT,STRING,BOOLEAN
carro = ["Fusca", "1.0", 15000, 1990, "São Paulo", True]

print(frutas)
print(letras)
print(vazio)
print(numeros)
print(carro)


#Usar um numero dentro de uma lista retorna o valor correspondente a posição do numero
print(frutas[0])
print(frutas[-1])

#Matriz é apenas o nome dado para LISTA ANINHADAS, que se trata de uma lista dentro de outra lista
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[0])
print(matriz[0][0])
print(matriz[1][2])
print(matriz[-2][-2])

#FATIAMENTO de LISTA, denomina por onde se inicia, onde termina, e as paradas ou valores que serão pulados
nome = list("GUSTAVO")

print(nome[2:])
print(nome[:2])
print(nome[0:4])
print(nome[0:8:2])
print(nome[::])
print(nome[::-1])

#FOR é usada para percorrer uma LISTA, e mostrar o valores dela
carros = ["GOL", "PALIO", "UNO", "FUSCA", "MAREA"]
for veiculo in carros:
    print(veiculo)
#ENUMERATE percorre a LISTA numerando os valores da LISTA    
for indice, veiculo in enumerate(carros):
    print(f"{indice}: {carros}")
#OBS: Para FOR deve se declarar uma variavel para percorrer a lista exemplo INDICE, VEICULO é a variavel que percorre pela LISTA carros   

#FILTROS em LISTAS
valores = list(range(50))
pares = []
impares = []
potencia = []

#Primeiro metodo que pode ser usado é o APPEND, percorrendo um for pode se criar um filto e colocar os valores filtrados dentro de outra LISTA
for num in valores:
    if num % 2 == 0:
        pares.append(num)
print(pares)

#Segundo metodo pode ser executado dentro da lista, sem a necessidade de APPEND
impares = [num for num in valores if num % 2 != 0]
print(impares)

for num in valores:
    potencia.append(num ** 2)
print(potencia)
