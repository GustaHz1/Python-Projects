funcionario = {}

while True:
    opcao = int(input(" [1]Cadastrar\n [2]Listar\n [3]Editar nome\n [4]Remover por nome\n [5]Sair\n"))

    if opcao == 1:
        nome = input("Nome do funcionário: ")
        setor = input("Setor: ")
        turno = input("Turno: ")
        juncao = [setor, turno]
        funcionario[nome] = juncao
        
    elif opcao == 2:
        for chave, valor in funcionario.items():
            print(chave, valor, "\n")
            
    elif opcao == 3:
        nome = input("Digite o nome que deseja alterar: ")
        if nome in funcionario.keys():
            novo_nome = input("Digite o novo nome: ")
            nome_antigo = funcionario.pop(nome)
            funcionario[novo_nome] = nome_antigo
            print("Nome alterado! \n")
        else:
            print("Funcionario não encontrado!  \n")
            
    elif opcao == 4:
        nome_remover = input("Digite o nome a ser removido: ")
        if nome_remover in funcionario.keys():
            funcionario.pop(nome_remover)
            print("Funcionario removido! \n")
        else:
            print("Funcionario não encontrado! \n")
            
    elif opcao == 5:
        break

    else:
        print("Valor não encontrado!")
            