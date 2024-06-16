class Operacoes:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


class Somar(Operacoes):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)  
    

    def adicao(self):
        return self.num1 + self.num2
    

soma = Somar(1 ,2)
soma.adicao()
print(soma)
        



