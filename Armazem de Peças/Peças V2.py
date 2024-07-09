# Classe principal que definimos nossos dicionários!
class Pecas:
    # Construtor inicial com os dicionários
    def __init__(self, pecas_valor = None, pecas_quantidade = None):
        if pecas_valor is None:
            self.pecas_valor = {}
        else:
            self.pecas_valor = pecas_valor
        
        if pecas_quantidade is None:
            self.pecas_quantidade = {}
        else:
            self.pecas_quantidade = pecas_quantidade


    def adicionar_pecas_valor(self, chave, valor):
        self.pecas_valor[chave] = valor


    def adicionar_pecas_quantidade(self, chave, quantidade):
        self.pecas_quantidade[chave] = quantidade

    # Função para visualizar os dicionários
    def visualizar(self):
        print("Quantidade de Peças", self.pecas_quantidade)
        print("Valores das Peças", self.pecas_valor)
    

#Classe da opção 1 (Armazenar)
class Armazenar(Pecas):
    def __init__(self, pecas_valor = None, pecas_quantidade = None):
        super().__init__(pecas_valor, pecas_quantidade)


    # Função que chama a função de adicionar da classe pai passando os valores a serem adicionados!
    def registrar_pecas(self, chave, valor, quantidade):
        self.adicionar_pecas_valor(chave, valor)
        self.adicionar_pecas_quantidade(chave, quantidade)
        print(f"Peça {chave} adicionada com sucesso! \n")


# Classe da opção 2 (Contagem)
class Contagem(Pecas):
    def __init__(self, pecas_valor = None, pecas_quantidade = None):
        super().__init__(pecas_valor, pecas_quantidade)

    # Função com o objetivo de contar as peças utilizando o metodo enumerate
    def contar_pecas(self, contagem):
        if contagem in self.pecas_quantidade:
            total_pecas = self.pecas_quantidade[contagem]
            for indice, _ in enumerate(range(1, total_pecas + 1), 1):
                print(indice, "\n")
        else:
            print("Peça invalida! \n")

# Classe da opção 3 (Remover)
class Remover(Pecas):
    def __init__(self, pecas_valor = None, pecas_quantidade = None):
        super().__init__(pecas_valor, pecas_quantidade)

    # Função responsável por remover os valores do dicionário através do .pop
    def remover_pecas(self, remover):
        if remover in self.pecas_valor:
            self.pecas_valor.pop(remover)
            self.pecas_quantidade.pop(remover)
            print(f"Peça {remover} removida com sucesso! \n")

        else:
            print("Peça inexistente! \n")

# Classe da opção 4 (Comprar)
class Compra(Pecas):
    def __init__(self, pecas_valor = None, pecas_quantidade = None):
        super().__init__(pecas_valor, pecas_quantidade)

    # Função responsável pela compra, verificando a quantidade de peças e somando os valores
    def comprar_pecas(self, compra, total):
        if compra in self.pecas_quantidade:
            if self.pecas_quantidade[compra] > 0:
                self.pecas_quantidade[compra] -= 1
                total += self.pecas_valor[compra]
                print(f"Peça {compra} comprada com sucesso! Peças restantes: {self.pecas_quantidade[compra]}")
            else:
                print("Peça sem estoque!")
        else:
            print("Peça não encontrada")
        return total


pecas_valor = {}
pecas_quantidade = {}


store = Armazenar(pecas_valor, pecas_quantidade)
score = Contagem(pecas_valor, pecas_quantidade)
remove = Remover(pecas_valor, pecas_quantidade)
purchase = Compra(pecas_valor, pecas_quantidade)
parts = Pecas(pecas_valor, pecas_quantidade)


# As funções abaixo são responsáveis pelos valores de entrada
def viusalizar_pecas(parts):
    parts.visualizar()
    

def armazenar_pecas(store):
    chave = input("Digite o nome da peça que deseja adicionar: \n")
    valor = int(input("Digite o valor unitário da peça: \n"))
    quantidade = int(input("Digite a quantidade de peças que deseja armazenar: \n"))
    store.registrar_pecas(chave, valor, quantidade)


def contar(score):
    contagem = input("Qual peça deseja contar: \n")
    score.contar_pecas(contagem)


def removendo_pecas(remove):
    remover = input("Qual peça deseja remover: \n")
    remove.remover_pecas(remover)

def comprando_pecas(purchase):
    total = 0
    while True:
        compra = input("Qual peça deseja comprar (ou digite 'sair' para encerrar): ")
        if compra == 'sair':
            print(f"Total da compra: R$ {total:.2f}")
            break
        else:
            total = purchase.comprar_pecas(compra, total)


# loop While realizando a verificação da opção desejada pelo cliente
while True:
    print('''
          [1]Armazenar
          [2]Contagem
          [3]Remover
          [4]Comprar
          [5]Visualizar
          [6]Sair
          \n''')
    
    acao = input("\nQual ação deseja realizar: \n")
    if acao == '1':
        armazenar_pecas(store)

    elif acao == '2':
        contar(score)
    
    elif acao == '3':
        removendo_pecas(remove)

    elif acao == '4':
        comprando_pecas(purchase)

    elif acao == '5':
        viusalizar_pecas(parts)

    elif acao == '6':
        break

        

        