month = int(input("Digite um mes: "))
#O dicionário em Python separa a chaves e após isso o valor que cada chave representa
months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
  }
#A variavel MONTH percore o dicionário e se o valor digitado na variável for igual a de alguma chave do dicionário, será mostrado o valor da chave
if month in months_dict.keys():

 print(months_dict[month])

  
valor = input()

quantidade = len(valor)

if quantidade <= 140:
  print("TWEET")
else:
  print("MUTE")

