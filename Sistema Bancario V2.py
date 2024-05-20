print("-" * 30)
print("Bem vindo ao banco!")   
print("-" * 30, "\n")


usuarios = []
contas = []

#FUNÇÃO para criar um novo usuario
def criar_usuario():
    global usuarios 
    logradouro = input("Digite seu logradouro: ")
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    cpf = input("Digite seu CPF: ")
    for usuario in usuarios:
        #Verificação se já existe um usuario cadastrado com o CPF informado 
        if usuario['cpf'] == cpf:
            print("Usuário já cadastrado!","\n")

    #Criação de um DICIONARIO para armazenar o usuario 
    novo_usuario = {
        'logradouro': logradouro,
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf
    }
    #O DICIONARIO criado é armazenado na lista, utilizando o comando APPEND
    usuarios.append(novo_usuario)
    print(f"Usuário cadastrado: {cpf}","\n")
    return cpf

#FUNÇÃO para criar uma nova conta
def criar_conta():
    global contas
    usuario_cpf = input("Digite o CPF do usuário: ")
    #O FOR percorre a lista verificando se existe usuario dentro da lista, após isso o if verifica se o CPF digitado está igual a algum CPF da lista
    for usuario in usuarios:
        if usuario['cpf'] == usuario_cpf:
            numero_conta = len(contas) + 1
            #Ao criar a conta o programa armazena as informações dela em um DICIONARIO
            nova_conta = {
                'agencia': "0001",
                'numero_conta': numero_conta,
                'cpf': usuario_cpf,
                'usuario': usuario
            }
            #O DICIONARIO criado é armazenado na lista, utilizando o comando APPEND
            contas.append(nova_conta)
            print("Conta criada com sucesso!""\n")
            print(f"Agência: {nova_conta['agencia']} Numero da conta: {nova_conta['numero_conta']}","\n")
            return nova_conta

    print("Usuário não cadastrado!","\n")
 

while  True:

    print(""" 
      ============================ 
      |                          |
      |[1]Criar usuario          |
      |[2]Criar conta            |
      |[3]Login                  |
      |                          |
      |                          |
      |                          |
      |                          |
      ============================
      """)
    login = int(input("Qual operação deseja realizar: "))

    if login == 1:
        criar_usuario()
    elif login == 2:
        criar_conta()
    elif login == 3:
        break

    






#FUNFÇÃO para executar depósitos
def depositar(saldo, extrato):
    deposito = float(input("Quanto deseja depositar: "))
    if deposito > 0:
        saldo += deposito
        extrato += f"Deposito: R$ {deposito:.2f}\n"
        print("Deposito realizado\n")
    else:
        print("Operação invalida, valor negativo!\n")
    return saldo, extrato

#FUNÇÃO para executar saques
def sacar(saldo, extrato, saque_diario, numero_saque, limite_saque):
    if saque_diario < numero_saque:
        saque = float(input("Quanto deseja sacar: "))
        if saque > saldo:
            print("Saldo insuficiente \n")
        elif saque > limite_saque:
            print("O saque ultrapassa o limite \n")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            saque_diario += 1
            print("Saque realizado \n")
        else:
            print("Operação inválida, valor negativo! \n")
    else:
        print("Número de saques superior ao permitido \n")
    return saldo, extrato, saque_diario

#FUNÇÃO para retornar as operações realizadas 
def mostrar_extrato(saldo, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

saldo = 0
extrato = ""
saque_diario = 0
numero_saque = 3
limite_saque = 500

while True:
    opcao = input("Qual operação deseja realizar ([1]: Depositar, 2: Sacar, 3: Extrato, 0: Sair): ")
    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, saque_diario = sacar(saldo, extrato, saque_diario, numero_saque, limite_saque)
    elif opcao == "3":
        mostrar_extrato(saldo, extrato)
    elif opcao == "0":
        break
    else:
        print("Opção invalida, digite novamente: ") 