from _tkinter import tk

while True:

    encerrar = input("Deseja encerra: ")
    if encerrar == 'sim':
        break

    else:
        numerador = float(input())
        operacao = input()
        denominador = float(input())

        if operacao == '+':
            print(numerador + denominador)

        elif operacao == '-':
            print(numerador - denominador)

        elif operacao == '*':
            print(numerador * denominador)

        elif operacao == '/':
            print(numerador / denominador)

        elif operacao == '%':
            print(denominador * (numerador / denominador))

        else:
            print("Operação invalida! ")

