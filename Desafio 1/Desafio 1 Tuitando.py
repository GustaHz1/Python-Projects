#LEN é usado para realizar a contagem de caracter de uma variável
valor = input()

quantidade = len(valor)

if quantidade <= 140:
  print("TWEET")
else:
  print("MUTE")
