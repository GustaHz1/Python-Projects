#SET é um método que é usado para quando não queremos que valores se repitam
#SET pode ser declarado com uma LISTA
numeros = set([1,2,3,4,5,6,7,8,9,1,2,3,4])
print(numeros,"\n")

nome = set("Gustavo")
print(nome,"\n")

#SET pode ser declarado com um TUPLE
cores = set(("Verde", "Vermelho", "Azul", "Verde", "Azul",))
print(cores,"\n")

#SET pode ser declarado com "{}"
linguagens = {"Python", "Java", "C#", "Java"}
print(linguagens,"\n")

#Para acessar valores de um SET é necessário converter ele para LISTA
dias = {"Segunda", "Terça", "Quarta"}
dias = list(dias)
print(dias[0],"\n")

#UNION tem como função juntar CONJUNTOS/SET
conjunto_a = {"Gustavo", "Henrique"}
conjunto_b = {"Aparecido", "Alfredo"}
union = conjunto_a.union(conjunto_b)
print(union,"\n")

#INTERSECTION tem como função juntar os valores iguais dos CONJUNTOS/SET
conjunto_c = {1,2,3,4,5,6}
conjunto_d = {2,4,6,8,10}
intersection = conjunto_c.intersection(conjunto_d)
print(intersection,"\n")

#DIFERENCE OU SYMMETRIC_DIFF tem como função mostrar os valores diferentes entre dois CONJUNTOS/SET
conjunto_e = {"Azul", "Verde", "Vermelho"}
conjunto_f = {"Preto", "Vermelho", "Verde"}
difference = conjunto_e.symmetric_difference(conjunto_f)
print(difference,"\n")

#ISSUBSET/ISSUPERSET tem como função comparar se os valores de um CONJUNTO/SET são iguai ao de outro
conjunto_g = {1, 2, 3, 4, 5,6 }
conjunto_h = {2,4,6}
issubset = conjunto_g.issubset(conjunto_h)
issuperset = conjunto_h.issuperset(conjunto_g)
print(issubset)
print(issuperset,"\n")

#ISDISJOINT tem como função comparar se CONJUNTOS/SET são iguais
conjunto_i = {0,1,2,3,4}
conjunto_j = {5,6,7,8,9}
conjunto_k = {0,1}
isdisjoint = conjunto_i.isdisjoint(conjunto_j)
isdisjoint_1 = conjunto_i.isdisjoint(conjunto_k)
print(isdisjoint)
print(isdisjoint_1,"\n")

#ADD tem como função adicionar um valor em CONJUNTO/SET que não se repita
conjunto_l = {1,5,10,15}
print(conjunto_l)
conjunto_l.add(20)
print(conjunto_l)
conjunto_l.add(5)
print(conjunto_l,"\n")

#CLEAR tem como função limpar os valores de um CONJUNTO/SET
conjunto_m = {"Gustavo"}
print(conjunto_m)
conjunto_m.clear()
print(conjunto_m,"\n")

#COPY tem como função criar a copiá de um CONJUNTO/SET
conjunto_n = {"LOL","DOTA","CSGO"}
conjunto_n.copy()

#DISCARD tem como função retirar um valor específico de um CONJUNTO/SET
conjunto_o = {1,2,3,4,5,6,7,8,9,10,1,3,5}
print(conjunto_o)
conjunto_o.discard(1)
print(conjunto_o)
conjunto_o.discard(10)
print(conjunto_o,"\n")

#POP tem como função retirar o último valor de um CONJUNTO/SET
conjunto_p = {"Gustavo","Henrique","Aparecido","Alfredo"}
print(conjunto_p)
conjunto_p.pop()
print(conjunto_p,"\n")

#REMOVE tem como função remover um valor de um CONJUNTO/SET, porém ele não aceita valores inexistentes
conjunto_q = {1,2,3,4,5,6,7,8,9}
print(conjunto_q)
conjunto_q.remove(5)
print(conjunto_q,"\n")

#LEN tem como função conta a quantidade de valores em um CONJUNTO/SET
conjunto_r = {"LOL","DOTA","CSGO"}
qtd = len(conjunto_r)
print(f"A quantidade de valores em seu conjunto é {qtd}","\n")

#IN tem como função buscar se tem um valor dentro de um CONJUNTO/SET
conjunto_s = {"FIFA","BOMBA PATCH"}
possui = "FIFA" in conjunto_s 
n_possui = "PES" in conjunto_s
print(possui)
print(n_possui)