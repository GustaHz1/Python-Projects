class animal:
    #__INIT__ é o METODO de inicio de uma classe, atribuimos caracteristicas da classe dentro do __INIT__
    def __init__(self, tipo, alimentacao, cor, nome):
        self.tipo = tipo
        self.alimentacao = alimentacao
        self.cor = cor
        self.nome = nome

    #__DEL__ é executado no final da CLASSE, encerando todos os outros processos anteriores, podemos utiliar ele para mostrar alguma mensagem no final 
    def __del__(self):
        print("Removendo a instância da classe")


 #Este METODO por sua vez atualiza de junto com as atualizações da classe
    #self.__class__.__name__, utiliza a CLASSE pelo seu nome, qualquer alteração no nome da CLASSE não prejudica o codigo
    #Criamos um FOR para buscar as variaveis e seus valores "CHAVE" "VALOR"
    #Apos percorrer o FOR as variaveis e seus valores são adicionados em uma lista com o self.__dict__
    def __str__(self):
        return  f"{self.__class__.__name__}: {([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


tiger = animal("Tigre", "Carnivoro", "Laranja", "Osvaldo")
print(tiger)

print("TESTE")

#Forma para executar o DEL antes do final
del tiger

print("TESTE")
print("TESTE")
print("TESTE")