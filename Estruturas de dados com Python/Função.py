#Toda FUNÇÃO deve conter em sua declaração o construtor DEF
#FUNÇÔES tem como objetivo executar uma sequência de códigos, podendo receber variaveis
def mensagem():
    print("Aprendendo sobre função!")

#A FUNÇÃO pode receber uma variavel sem declarar o valor, porém é necessário que quando for chamar a FUNÇÂO declarar um valor
def mensagem_2(nome):
    print(f"Olá me chamo {nome}")    

#FUNÇÃO declarada com variavel e seu valor
def mensagem_3(nome = "Gustavo"):
    print(f"Olá me chamo {nome}")

mensagem()
mensagem_2(nome = "Henrique")
mensagem_3("\n")           

#Uma FUNÇÃO pode retornar valores, sendo operações entre outros, no entanto deve sempre se usar o RETURN
def total(numeros):
    return sum(numeros)


def antecessor_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor

#Por padrão da linguagem caso não tiver o RETURN o valor a ser exibido será NONE
def vazio(valor):
    valor + 10


print(total([10,20,30]))
print(antecessor_sucessor(100))
print(vazio(40),"\n")


def carro(marca, modelo, ano, placa):
    print(f"Carro da montadora {marca} modelo {modelo} do ano de {ano} com a placa {placa}")

#OBS ao exebir/executar os valores de uma FUNÇÃO podemos exebi-los em DICIONÁRIO com "**" ou em TUPLE com "*"
#Primeira forma de definir mais de um valor em uma FUNÇÃO, porém os valores podem ser trocadas de ordem
carro("Honda", "City", 2013, "EFG-3454") 
#Segunda forma de definir mais de um valor em uma FUNÇÃO, porém as variaveis podem ser trocadas ocasionando erros no códgio
carro(marca = "Fiat", modelo = "Siena", ano = 2005, placa = "hij-9981")
#Terceira forma de definir mais de um valor em uma FUNÇÃO, transformando os valores em DICIONÁRIOS/DICT usando "**"
carro(** {"marca": "Toyota", "modelo": "Corola Manual", "ano": 2018, "placa": "cod-2018"})   
print()

#Ao criar uma FUNÇÃO utilizado "/" está FUNÇÃO fara com que os valores que forem adicionados seguirão a ordem da FUNÇÃO
def criar_carro (modelo, ano, placa, marca, motor, combustivel, /,):
    print(modelo, ano, placa, marca, motor, combustivel, "\n")

criar_carro("City", 2013, "EDG-2021", "Honda", "1.6", "Etanol",)

#Ao criar uma FUNÇÃO utilizando "*" está FUNÇÃO exigirá que cada valor seja atribuida em seu devido local
def musica(*, nome, banda, almbum, duração, ano):
    print(nome, banda, almbum, duração, ano, "\n")

musica(nome = "In the End", banda = "Linkin Park", almbum = "Hybrid Theory", duração = "3:36", ano = 200)

#Forma para chamar os valores de uma FUNÇÃO ao realizar operações
def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def resultados(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")
    print(f"O resultado da operação {a} - {b} = {resultado}")
    
resultados(10, 10, soma)
resultados(10, 5, subtrair)
print()

#Para utilizar uma variavel dentro de uma FUNÇÃO cujo não foi declarada na mesma é necessário utilizar GLOBAL 
valor = 700

def saldo(bonus):
    global valor
    valor += bonus
    return valor

saldo(500)
print(valor)