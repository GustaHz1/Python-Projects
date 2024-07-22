# Treinando o PEP 8


# Constantes
CONSTANT = 1000


# Variáveis
variavel = 10


# Listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]



# Para nomear classes não utilizamos o _ 
# Classes sempre devem começar com letras maiúsculas
class JuridicPerson:
    def __init__(self, message):
        self.message = message
        print(message)

# Forma correta de escrever nomes de funções, nomeando o que exatamente a função faz!
def Print_hi_with_message(name):
    print(f"HI1, {name}")


# Forma incorreta de escrever nomes de funções, apesar de descrever objetivo o nome não utiliza _ para facilitar a leitura!
def Printhiwithmessage(name):
    print(f"HI!, {name}")


# Nome da função sujestivo, embora seus argumentos não expressam a sua inteção!
def Average (x, y, z):
    t = (x + y) / z
    print(t)


# Nome da função e argumentos sujestivos!
def Student_average(note_one, note_two, divisor):
    average = (note_one + note_two) / divisor
    return average


JuridicPerson("Hello World")

Print_hi_with_message("Gustavo")

final_average = Student_average(10, 20, 2)
print(final_average)