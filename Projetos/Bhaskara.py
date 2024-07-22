import math


A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
print()

#Calculando o valor de Delta 
delta = (B**2) - (4 * (A * C))
print(f"Valor de delta = {delta} \n")

if delta <= 0:
    print("Não é possível calcular se o delta for menor ou igual a 0! \n")

else:
    #Calculando o valor do x
    x_positivo = (-B + math.sqrt(delta)) / (2 * A)
    x_negativo = (-B - math.sqrt(delta)) / (2 * A)

    print(f"Valor de x1 = {x_positivo} \n")
    print(f"Valor de x2 = {x_negativo} \n")

