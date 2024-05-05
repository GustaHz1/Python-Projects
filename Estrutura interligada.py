#Todo o codigo abaixo é exemplos de uso de IF,ELIF e ELSE
saldo = 2000
saldo_especial = 3000
saldo_black = 4000

conta = int(input("Selecione o tipo da sua conta: \n [1]-Conta normal \n [2]-Conta especial \n [3]-Conta black"))

saque = float(input("Digite quanto deseja sacar: "))

if conta == 1:
    if saldo >= saque:
     print("Saque realizado")
    elif saldo < saque:
     print("Saldo insuficiente")
elif conta == 2:
    if saldo_especial >= saque:
       print("Saque realizado")
    elif saldo_especial < saque:
       print("Saldo insuficiente")
elif conta == 3:
    if saldo_black >= saque:
       print("Saque realizado")
    elif saldo_black < saque:
       print("Saque realizado")
                  



