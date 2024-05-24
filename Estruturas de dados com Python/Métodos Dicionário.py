#CLEAR é utilizado para limpar os valores de um DICIONÁRIO/DICT
nomes = {
"Primeirso Nome": "Gustavo",
"Segundo Nome": "Henrique",
"Terceiro Nome": "Aparecido",
"Quarto Nome": "Alfredo"    
}
print(nomes)
nomes.clear()
print(nomes,"\n")

#COPY é utilizado para criar uma cópia de um DICIONÁRIO/DICT
estados = {
1: "São Paulo",
2: "Rio de Janeiro",
3: "Minas Gerais"
}
copia = estados.copy()
print(copia)
copia  = {1: "SP", 2: "RJ", 3: "MG"}
print(copia,"\n")

#GET é utilizado para buscar um valor no DICIONÁRIO/DICT
contatos = {
"gustavoalf@gmail.com": {"Nome": "Gustavo", "Idade": 18},
"henriqueapa@gmail.com": {"Nome": "Henrique", "Idade": 19}    
}
print(contatos.get("Telefone"))
print(contatos.get("Telefone", {"Chave não encontrada"}))
get = contatos.get("gustavoalf@gmail.com")
print(get,"\n")

#ITEMS é utilizado para retornar uma lista de tuple
valores = {
1: "Primeiro",
2: "Segundo",
3: "Terceiro"
}
print(valores.items(),"\n")

#KEYS é utilizado para percorrer pelas chaves de um DICIONÁRIO/DICT
chaves = {1: "Nome", "Dia": 7, 2: "Hora"}
print(chaves.keys(),"\n")

#POP é utilizado para remover uma chave 'informada' de um DIOCIONÁRIO/DICT
remover = {1: "LOL", 2: "DOTA", 3: "CSGO", 4: "VALORANT"}
remover.pop(1)
print(remover)
remover.pop(3)
print(remover)
print(remover.pop(3, "Chave não encontrada"),"\n")

#POPITEM é utilizado para remover uma chave não sendo necessário informar a chave a ser removida 
remover.popitem()
print(remover)
remover.popitem()
print(remover,"\n")

#SETDEFAULT é utilizado para adicionar uma chave com seu valor caso este valor não exista, não sendo possível trocar o valor de uma chave existente
carros = {1: "Gol", 2: "Palio", 3: "Celta"}
carros.setdefault(1, "Fox")
print(carros)
carros.setdefault(4, "Fox")
print(carros)

#UPDATE é utilizado para adicionar uma nova chave com valor ao seu DICIONÁRIO/DICT, podendo substituir um valor existente de uma chave 
carros.update({1: "Fiesta"})
print(carros,"\n")
contatos.update({"alfredo@gmail.com": {"Nome": "Alfredo", "Idade": 20}})
print(contatos,"\n")

#VALUE é utilizado para retornar apenas os valores de um DICIONÁRIO/DICT
dias = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sábado"}
print(dias.values(),"\n")

#IN é utilizado para verificar se determinada chave está dentro de um DICIONÁRIO/DICT
jogos = {
"Offline": {"Jogo Favorito": "Skyrim", "Série Favorita": "Dark Souls", "Atmosfera Favorita": "The Witcher"},
"Online": {"Mais jogo": "LOL", "RAIVA": "FIFA", "Menos jogo": "CSGO"}    
}
resultado =  "Offline" in jogos
print(resultado)
resultado_2 = "Campanha" in jogos
print(resultado_2)
resultado_3 = "Jogo Favorito" in jogos["Offline"]
print(resultado_3)
resultado_4 = "Não Jogo" in jogos["Online"]
print(resultado_4,"\n")

#DEl é utilizado para excluir uma chave de um DICIONÁRIO/DICT, também pode excluir um DICIOÁRIO
musicas = {
"Scorpions": {1: "Rock you Like a Hurricane", 2: "Still Loving you", 3:"Wind Of Change"},    
"Iron Maiden": {1: "The Trooper", 2: "Fear of Dark", "3": "Wasted Years"},    
"Black Sabbath": {1: "Paranoid", 2: "Iron Man", 3: "War Pigs"}
}
del musicas ["Iron Maiden"][1]
print(musicas)
del musicas ["Black Sabbath"]
print(musicas)