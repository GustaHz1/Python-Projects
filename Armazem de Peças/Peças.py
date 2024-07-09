#Sistema de armazenar peças com listas
'''peca = []

while True:'''

print('''
[1]Adicionar peça 
[2]Visualizar lista
[3]Remover peça
[4]Sair: ''')
    
'''opcao = input("\n")

#Validação das opções 
    if opcao == '1':
        nova_peca = input("Qual peça deseja adicionar: ")
        if nova_peca in peca:
            print("Peça já existente!\n")
        else:
            peca.append(nova_peca)
            print(f"{nova_peca} adicionado com sucesso! \n")
    elif opcao == '2':
        print(peca)
    elif opcao == '3':
        remove_peca = input("Qual peça deseja remover: ")
        if remove_peca not in peca:
            print("Peça inexistente!\n")
        else:
            peca.remove(remove_peca)
            print(f"{remove_peca} removido(a) com sucesso! \n")
    elif opcao == '4':
        break
    else:
        print("Opção invalida!\n")


pecas = {}
print(pecas,"\n")
for i in range(len(peca)):
    pecas[peca[i][0]] = peca[i][1:]

print(pecas)'''

pecas = {}
pecas_valor = {}

while True:

    menu = input('''-----INVENTÁRIO-----
[1]Armazenar Peças
[2]Contar Peças
[3]Remover Peças
[4]Visualizar Peças
[5]Vender Peças
[6]Sair
\n ''')
    print()
    
    if menu == '1':
        #Adicionando peças ao dicionário 
        chave = input("Qual a peça que deseja adicionar: ")
        quantidade = int(input("Qual a quantidade de peças que deseja adicionar: "))
        valor = int(input("Digite o valor unitário de cada peça: "))
        pecas_valor[chave] = valor
        pecas[chave] = quantidade
        print(pecas)
        print(pecas_valor, "\n")

    elif menu == '2':
        contagem = input("Qual peça deseja contar: \n")
        if contagem in pecas:
            quantidade = pecas[contagem]
            for indice, _ in enumerate(range(1, quantidade + 1), 1):
                print(indice)
        else:
            print(f"Peça {contagem} inexistente!")
            
    elif menu == '3':
        remover = input("Qual peça deseja remover da lista: ")
        pecas.pop(remover)
        print(f"Peça {remover} removida(o) com sucesso! \n")

    elif menu == '4':
        print(f"Peças {pecas} Quantidade")
        print(f"Peças {pecas_valor} Valor \n ")

    elif menu == '5':
        total = 0
        while True:
            compra = input("Qual peça deseja comprar (ou digite 'sair' para encerrar): \n").strip().lower()

            if compra == 'sair':
                print(f"Total da compra: R$ {total:.2f}\n")
                break

            elif compra not in pecas:
                print("Peça não encontrada. Tente novamente.")
                continue

            elif pecas[compra] > 0:
                pecas[compra] -= 1
                total += pecas_valor[compra]
                print(f"Você comprou um(a) {compra}. Quantidade restante: {pecas[compra]}")
            else:
                print("Peça sem estoque!")

            encerrar = input("Deseja continuar comprando? (Digite 'sair' para encerrar ou 'sim' para continuar): \n").strip().lower()
            if encerrar == 'sair':
                print(f"Total da compra: R$ {total:.2f}\n")
                break

    elif menu == '6':
        break

    else:
        print("Valor invalido! \n")

