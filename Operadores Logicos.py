
saldo = 500
saque = 200
limite = 100

#AND para retornar TRUE os dois valores tem que ser verdadeiros, se qualquer valor ser falso retorna FALSE
print(saldo >= saque and saque <= limite)

#OR apenas um valor sendo verdadeiro para retornar TRUE, dois valores sendo falsos para retornar FALSE
print(saldo >= saque or saque <= limite)

#PARENTESE é usado para facilitar o entendimento do código e priorizar a operação dentro do PARENTESE
conta = (saldo >= saque and saque <=limite) or (saque >= saldo and limite >= saque)
print(conta)

#NOT é usado para se referir ao contrário
print(not 1000 > 1500)

# IS é usado para verificar se as variáveis possuem o mesmo valor
nome = "python"
nome_2 = "python"
print (nome is nome_2)

