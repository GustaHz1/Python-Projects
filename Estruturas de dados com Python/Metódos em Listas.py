#OBS utilizar parenteses quando passar algum metodo da lista
#APPREND tem como objetivo adicionar algum elemento na lista
lista = []

lista.append(1)
lista.append("Gustavo")
lista.append([10,20,30])
print(lista,"\n")

#CLEAR tem como objetivo limpar os valores de uma lista
lista_2 = ["Henrique"]
print(lista_2)
lista_2.clear()
print(lista_2,"\n")

#COPY tem como objetivo criar uma copia da lista, fazendo que qualquer alteração nesta copia não altere a lista original 
lista_3 = lista_2.copy()
print(lista_3)
lista_3 = "Aparecido"
print(lista_3)
print(id(lista_3), id(lista_2),"\n")

#COUNT tem como objetivo contar a quantidade de um determinado valor em uma lista
lista_4 = ["Maça", "Uva", "Laranja", "Uva", "Laranja", "Laranja"]
maca = lista_4.count("Maça")
uva = lista_4.count("Uva")
laranja = lista_4.count("Laranja")
print(f"Quantas Maças tem na lista {maca}")
print(f"Quantas Uvas tem na lista {uva}")
print(f"\nQuantas Laranjas tem na lista {laranja}")

#EXTEND tem como objetivo adicionar mais de um valor a uma lista, podendo mesclar listas 
lista_5 = ["Gustavo", "Henrique"]
print(lista_5)
lista_5.extend(["Aparecido", "Alfredo"])
print(lista_5,"\n")

#INDEX tem como objetivo apontar o local da primeira aparição de um determinado valor
lista_6 = ["Vermelho", "Azul", "Verde", "Azul", "Preto"]
print(lista_6.index("Azul"))
print(lista_6.index("Preto"))
print()

#POP tem como objetivo retirar o ultimo valor de uma lista, execeto se for passado um indice a POP
lista_7 = ["Uno","Palio","Gol"]
lista_7.pop()
print(lista_7)
lista_7.pop(0)
print(lista_7,"\n")

#REMOVE tem como objetivo retirar a primeira ocorrencia de uma valor estipulado 
lista_8 = ["Python", "Java", "C", "C#"]
lista_8.remove("Java")
print(lista_8,"\n")

#REVERSE tem como objetivo inverter os valores da lista
lista_9 = ["Gustavo", "Henrique", "Aparecido", "Alfredo"]
lista_9.reverse()
print(lista_9,"\n")

#SORT tem como objetivo organizar a lista
lista_10 = ["Gustavo", "Bianca", "Rafaela", "Enzo", "Teo", "Ravi"]
lista_10.sort()
print(lista_10,"\n")

#LEN tem como objetivo contar a quantidade de valores dentro de uma lista
lista_11 = ["Já", "Não", "Tenho", "Ideia", "De", "Padrões"]
quantidade = len(lista_11)
print(quantidade,"\n")

#SORTED tem como objetivo organizar a lista, no entanto é uma função que pode ser chamada a qualquer momento
lista_12 = ["HONDA", "FORD", "FIAT", "HYUNDAI", "TOYOTA"]
#Realiza a organização da lista da palavra com maior caracter para a menor 
print(sorted(lista_12, key = lambda x: len(x)))


