class Conta:
    def __init__(self, nmr_agencia, saldo):
        #Ao declarar uma variavel utilizando _nome variavel, estamos referindo que a variavel é privada, podendo ser acessada e modificada apenas na sua classe
        self._saldo = saldo
        self.nmr_agencia = nmr_agencia
        
    def depositar(self, valor):
        self._saldo += valor

    
    def sacar(self, valor):
        self._saldo -= valor


    def mostrar_saldo(self):

        return self._saldo  
    
#Podemos criar METODOS com a variavel, sendo dentro da sua CLASSE, o Python não proibi de você utilizar a variavel fora da classe, mas como boa prática não utilizamos fora da CLASSE
conta = Conta("0001", 100)
#Forma errada de exibir a variavel
print(conta._saldo)
conta.depositar(100)
print(conta.nmr_agencia)
#Para exibir a variavel devemos criar um METODO para mostrar a variavel e não chamar ela pelo seu nome 
print(conta.mostrar_saldo())