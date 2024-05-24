#Existe duas maneiras de declarar um dicionário em Python
#Primeira maneira definir uma variavel e com {} dar ínicio, declarando uma chave e após isso o valor
dados = {"nome": "Gustavo", "idade": 18}
print(dados,"\n")

#Segunda maneira definir com o construtor DICT, utilizando () defina a chave e um valor 
pessoa = dict(nome = "Gustavo", idade = 18)
print(pessoa,"\n")

#Forma de adicionar uma nova chave para o seu  DICIONÁRIO/DICT
pessoa["sobrenome"] = "Alfredo"
print(pessoa,"\n")

#Forma para substituir valores de um DICIONÁRIO/DICT
pessoa["nome"] = "Henrique"
pessoa["idade"] = 20
pessoa["sobrenome"] = "Aparecido"
print(pessoa,"\n")

#DICIONÁRIO/DICT aninhado, podendo conter mais de um DICIONÁRIO
email = {
"gustavo@gmail.com":{"nome": "Gustavo", "idade": 18, "telefone": "1987-6543"},
"henrique@gmail.com":{"nome": "Henrique", "idade": 19, "telefone": "2789-3456"},
"aparecido@gmail.com":{"nome": "Aparecido", "idade": 99, "telefone": "3654-1987"},
"alfredo@gmail.com":{"nome": "Alfredo", "idade": 20, "telefone": "4653-8179"}      
}
print(email["alfredo@gmail.com"],"\n")

#Formas de percorrer todo o DICIONÁRIO/DICT
for chave in email:
    print(chave, email[chave],"\n")

#Percorrendo o DICIONÁRIO/DICT com o método ITEMS passando por cada chave do DICIONÁRIO/DICT
for chave, valor in email.items():
    print(chave, valor,"\n")    

#Forma de selecionar o valor de uma chave de um DICIONÁRIO/DICT 
contato = {
    1: ["Gustavo", 19, "1991-0090",],
    2: ["Henrique", 20, "2009-1234",],
    3: ["Aparecido", 99, "3190-1485",]
}

e = int(input("Digite o número do seu contato: "))
if e in contato.keys():
    print(contato[e])   
