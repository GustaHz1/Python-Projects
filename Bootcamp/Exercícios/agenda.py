agenda = {}

def cadastrar(chave, valor):
    agenda[chave] = valor
    
def remover(chave):
    if chave in agenda:
        agenda.pop(chave)
    else:
        print("Nome não encontrado!")
        
def exibir():
    if agenda:
        print("Contatos: ")
        for chave, valor in agenda.items():
            print(f"{chave} - {valor}")
    else:
        print("Agenda vazia!")

while True:
    opcao = int(input("[1]Cadastrar / [2]Remover / [3]Exibir [4]Parar "))
    if opcao == 1:
        chave = input("Digite o nome: ")
        valor = input("Digite o telefone: ")
        cadastrar(chave, valor)
        
    elif opcao == 2:
        chave = input("Digite o nome: ")
        remover(chave)
        
    elif opcao == 3:
        exibir()
        
    elif opcao == 4:
        break
    
    else:
        print("Valor invalido! ")
