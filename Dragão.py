c = int(input("Quantas operações deseja realizar: "))
for i in range(c):
    n = int(input("Digite um valor: "))
    if n > 8000 or n == 8000:
        print("Mais de 8000!")
    else:
        print("Inseto!")
        