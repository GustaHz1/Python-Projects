nome = "  Gustavo "
palavra = "CaIxA"
#UPPER é usado para formatar a STRING para maiusculo
print(palavra.upper())
#LOWER é usado para formatar a STRING para minusculo
print(palavra.lower())
#TITLE é usado para formatar a STRING para titulos
print(palavra.title())

#STRIP é usado para remover o espaço em branco 
print(nome.strip())
#LSTRIP é usado para remover o espaço em branco da ESQUERDA
print(nome.lstrip())
#RSTRIP é usado para remover o espaço em branco da DIREITA
print(nome.rstrip())

#CENTER é usado para adicionar caracteres em volta de sua STRING ou espaço em branco
print(palavra.center(11, "#"))
#JOIN é usado para adicionar carcteres em volta de cada CHAR de uma STRING
print(".".join(palavra))