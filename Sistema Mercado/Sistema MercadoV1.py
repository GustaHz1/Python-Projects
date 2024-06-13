class Produtos:
    #Criação do dicionario que armazena os produtos 
    def __init__(self, produtos=None):
        if produtos is None:
            self.produtos = {}
        else:
            self.produtos = produtos

    #Adicionando produtos no dicionario 
    def Criar_lista_de_produtos(self, chave, valor):
        self.produtos[chave] = valor

    #Metodo para visualizar os produtos cadastrados
    def visualizar_produtos(self):
        if not self.produtos:
            print("Não há produtos cadastrados.")
        else:
            print("\nLista de produtos:")
            for chave, valor in self.produtos.items():
                print(f"Produto: {chave}, Valor: R${valor:.2f}")

#Classe de login ADM
class Administrador(Produtos):
    #Metodo para registrar produtos, o metodo chama o metodo da classe pai passando a chave e valor inserido pelo usuario e cadastrando um novo produto
    def registrar_produtos(self, chave, valor):
        self.Criar_lista_de_produtos(chave, valor)
        print(f"Produto {chave} registrado com sucesso!")

    #Metodo que realiza a troca do valor de um produto cadastrado, o metodo altera o valor da chave do dicionario
    def alterar_valor(self, chave, novo_valor):
        if chave in self.produtos:
            self.produtos[chave] = novo_valor
            print(f"Valor do produto {chave} alterado para R${novo_valor:.2f}.")
        else:
            print(f"Produto {chave} não encontrado.")


class Cliente(Produtos):
    #Realiza a compra de produtos cadastrados, no final exibe o valor total da compra
    def comprar_produtos(self, chave):
        if chave in self.produtos:
            print(f"Produto: {chave}, Preço: R${self.produtos[chave]:.2f}")
            return self.produtos[chave]
        else:
            print("Produto não encontrado!\n")
            return 0.0

#Menu de login cliente
def Menu_cliente():
    menu_cliente = """\n
    [CO] Comprar 
    [VI] Visualizar Produtos
    [S] Sair
    """
    return input(menu_cliente)

#Menu de login ADM
def Menu_Adm():
    menu_adm = """\n
    [CP] Cadastrar Produto
    [AV] Alterar Valor
    [VI] Visualizar Produtos
    [S] Sair
    """
    return input(menu_adm)


#Lista criada para armazenar os produtos criados em ADM para que o Cliente possa comprar
produtos_compartilhados = {}

#Variaveis recebendo uma classe para trabalhar dentro de funções
admin = Administrador(produtos_compartilhados)
cliente = Cliente(produtos_compartilhados)

#Função para cadastrar produto, pega as informações do produto como nome e valor e retorna para o metodo assim adicionando a lista
def cadastrar_produto(admin):
    chave = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    admin.registrar_produtos(chave, valor)

#Função que percore a lista procurando o produto inserido e se econtrar um produto pede um novo valor
def alterar_valor_produto(admin):
    chave = input("Digite o nome do produto: ")
    novo_valor = float(input("Digite o novo valor do produto: "))
    admin.alterar_valor(chave, novo_valor)

#Função que percorre a lista procurando o produto inserido e somando o valor 
def comprar(cliente):
    total = 0
    while True:
        produto = input("Qual produto deseja comprar: (Digite sair para encerrar) \n")
        if produto == 'sair':
            print(f"Valor da compra R${total:.2f}")
            break
        total += cliente.comprar_produtos(produto)

#Função para visualizar os produtos da lista
def visualizar_produtos(cliente):
    cliente.visualizar_produtos()

#Loop principal, dentro do loping o usuario realiza o login e as operações disponiveis 
while True:
    login = input('''\n
      =========Bem Vindo========== 
      |                          |
      |[1] Cliente               |
      |[2] Administrador         |
      |[0] Sair                  |
      |                          |
      |                          |
      |                          |
      |                          |
      ============================
      ''')
    
    #Validação de função a ser executada, realiza a verificação do valor inserido pelo usuario e executa de acordo com o valor
    if login == '1':
        while True:
            opcao = Menu_cliente().lower()
            if opcao == "co":
                comprar(cliente)
            elif opcao == "vi":
                visualizar_produtos(cliente)
            elif opcao == 's':
                break
            else:
                print("Entrada inválida!")
    elif login == '2':
        while True:
            opcao = Menu_Adm().lower()
            if opcao == 'cp':
                cadastrar_produto(admin)
            elif opcao == 'av':
                alterar_valor_produto(admin)
            elif opcao == "vi":
                visualizar_produtos(admin)
            elif opcao == 's':
                break
            else:
                print("Entrada inválida!")
    elif login == '0':
        break
    else:
        print("Entrada inválida!")