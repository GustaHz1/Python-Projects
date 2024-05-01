
extrato = ""
saque = 0
deposito = 0
saldo = 0
limite_saque = 500
saque_diario = 0
numero_saque = 3

print(""" 
      =========Bem Vindo========== 
      |                          |
      |[1]Depositar              |
      |[2]Sacar                  |
      |[3]Extrato                |
      |[0]Sair                   |
      |                          |
      |                          |
      |                          |
      ============================
      """)

while True:

    opcao = input("Qual operação deseja realizar: ")
#Opção 1 realiza o depósito, validando se o valor não é negativo 
    if opcao == "1":
      deposito = float(input("Quanto deseja Depositar: "))
      if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("Deposito realizado\n")
      else:
        print("Operação inválida, valor negativo!\n")
#Opção 2 realiza a opção saque, validando o limite de saque, o saldo e valor negativo
    elif opcao == "2":
         if saque_diario < numero_saque:
           saque = float(input("Quanto deseja sacar: "))
           if saque > saldo:
             print("Saldo insuficiente \n") 
           
           elif saque > limite_saque:
             print("O saque ultrapassa o limite \n")
           
           elif saque > 0: 
             print("Saque realizado \n")
             saldo -= saque   
             extrato += f"Saque: R$ {saque:.2f}\n"
             saque_diario += 1
           
           else:
             print("Operação inválida, valor negativo! \n")
         else:
            print("Número de saque superior ao permitido \n")
#Opção 3 mostra o extrato, informando todas as operações realizadas e seu saldo
    elif opcao == "3":
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")      
      
    elif opcao == "0":
       break

    else:
       print("Opção inválida digite novamente \n")
      
