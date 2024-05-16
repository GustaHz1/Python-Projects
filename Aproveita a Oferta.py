T = int(input("Quantas compras serão feitas: "))

for i in range(T):
    n = (input("Quantidade de garrafas compradas e quantidade de vazias para uma nova:  "))
    x = n.split()
    a =  x[0]
    b =  x[1]
    a = int(a)
    b = int(b)
    div = a // b
    mod = a % b
    total = div + mod
    print(total)
