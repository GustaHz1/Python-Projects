#Primeira forma com dois valores de entrada, e fazendo o comparativo dos digitios finais de um determinado valor
n = int(input("Digite o total de operações que deseja realizar: "))

while (n > 0):

  a = input("Digite um valor: ")
  b = input("Digite outro valor: ")

#Utilizando o método SLICING, utilizado para separar os caracteres de uma variavel
  digitos_a = a[-4]
  digitos_b = b[-4]

  if digitos_b == digitos_a:
    print("encaixa")
  else:
    print("nao encaixa")       
  n -= 1


#Segundo metodo com um valor de entrada e atribuindo o valor a duas LISTAS
m = int(input("Digite o total de operações que deseja realizar: "))

while (m > 0):

  entrada = input().split(" ")

  a = entrada[0]
  b = entrada[1] 

#ENDSWITH realiza um comparativo de variáveis, comparando um valor estipulado pelo metodo
  if len(b) > len(a):
    print("nao encaixa")
  elif a.endswith(b):
    print("encaixa")
  else:
    print("nao encaixa")  
  m -= 1
    
    