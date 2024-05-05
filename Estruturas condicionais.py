
saldo = 2000.0
#Pode se criar uma VARIAVEL junto ao comando INPUT, determinando o tipo da VARIAVEL antes de INPUT
saque = float(input("Informe o valor do saque: "))

#Não é necessário o uso de CHAVES, no entanto para o código funcionar é necessário que esteja orientado de maneira correta
if saldo >= saque: 
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")    



saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")

#Pode se usar vários ELIF para denominar condiçõesa
opcao = int(input("Selecione a ação que quer fazer, [1]-Sacar \n [2]-Depositar \n [3]-Verificar saldo "))    

if opcao == 1:
    print("Quanto deseja sacar?")

elif opcao == 2:
    print("Quanto deseja depositar?")

elif opcao == 3:
    print(saldo)

