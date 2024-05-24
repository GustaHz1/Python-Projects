
#Metodos para exibir uma frase utilizando sua váriavel STRING
#Metodo 1 e menos utilizado é o %, S para STRING, D para INT, F para FLOAT
nome = "Gustavo"
idade = 18
profissao = "Armazenista"
cidade = "Americana"

print("Olá, me chamo %s, eu tenho %d anos de idade, trabalho como %s, atualmente moro na cidade de %s." % (nome,idade,profissao,cidade))
print()
#Metodo 2 é o FORMAT,possivel alterar a variavel utilizando numeracao nos {} ou o nome da variavel
print("Olá, me chamo {0}, eu tenho {1} anos de idade, trabalho como {2}, atualmente moro na cidade de {3}." .format(nome,idade,profissao,cidade))
print()
#Metodo 3 o mais utilizado é o F-STRING, dentro de colchetes coloque o nome da variavel, e no inicio do print coloque a letra f
print(f"Olá, me chamo {nome}, eu tenho {idade} anos de idade, trabalho como {profissao}, atualmente moro na cidade de {cidade}.")
print()

#Forma de formatar numeros, adicionando ou removendo casas decimais, apos definir a variavel a ser apresentada utilize : e .f com o valor de casas a ser modificada
valor = 3.141457
saldo = float(input("Digite seu saldo: "))
print(f"Seu saldo é de {saldo:.2f}")
print(f"Seu valor é de {valor:.2f}")



#Fatiamento de STRINGS, usado para exibir um caracter ou caracteres especificos de uma STRING
print(nome[0])
print(nome[0:7])
print(nome[2:])
print(nome[6:8])
print(nome[3:8:2])
print(nome[:])
print(nome[ ::-1])

# 3 aspas duplas ou simples faz que o print matenha os recuos e espaços estabelecidos
mensagem = f"""
    Olá meu nome é {nome},
tenho {idade} anos de idade,
      gosto de ouvir musicas.
"""
print(mensagem)     

print("""|======MENU======|

 1-Comprar
 2-Vender
 3-sair
|================|
""")