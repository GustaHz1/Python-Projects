#CLASSE PAI, nomeclatura que damos a uma CLASSE a qual sua FUNÇÕES são herdadas por outra
class alimento:
    #OBS uso de SELF para FUNÇÕES em CLASSES
    def __init__(self, tipo, nome, quantidade):
        self.tipo = tipo
        self.nome = nome,
        self.quantidade = quantidade

    def compar(self):
        print("Alimento selecionado para compra!","\n")


    def soma(soma):
        print("Soma dos alimentos comprados é:","\n")


    def desconto(self):
        print("Desconto é:")
        print("Novo valor a ser cobrado: ","\n")

    #Utilizando a FUNÇÃO __STR__ dentro da CLASSE PAI fazemos com que as outras variaveis que recebem CLASSES possam ser exebidas em um PRINT
    def __str__(self):
        return  f"{self.__class__.__name__}: {([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


#CLASSES FILHAS, são CLASSES que herdam as FUNÇÔES da CLASSE PAI, no entanto uma CLASSE PAI não herda da FILHA-
class bebidas(alimento):
    #Para receber e chamar uma FUNÇÃO de uma CLASSE PAI usamos o SUPER() junto do nome da FUNÇÃO a ser trabalhada
    def __init__(self, tipo, nome, quantidade,estado):
        super().__init__(tipo, nome, quantidade)
        self.estado = estado
    #CLASSES FILHAS podem ter suas própias FUNÇÕES, essas FUNÇÕES só podem ser usadas por elas mesmo, ou caso ela se torna PAI de uma nova CLASSE
    def liquido(self):
        #Verificação do valor atribuido a variavel ESTADO
        print(f"É {'Liquido' if self.estado else 'Sólido'}")


class secos(alimento):
    pass

class frios(alimento):
    pass


bebida = bebidas("Refrigerante", "Fanta", "2 Litros", True)
#Formatação de uma mensagem com CLASSES, utilize a variavel declarada mais o atributo do METODO de uma CLASSE
print(f"Sua bebida é um {bebida.tipo} {bebida.nome} {bebida.quantidade}")
bebida.liquido()

seco = secos("Chocolate", "Trento", "200 gramas")
print(f"Seu {seco.tipo} é um {seco.nome} de {seco.quantidade }")
seco.desconto()
seco.soma()

frio = frios("Presunto", "Sadia", "1 kilo")
print(f"Seu {frio.tipo} é {frio.nome} de {frio.quantidade}")
frio.compar()   

print(bebida)
print(seco)
print(frio)
        