class carro:
    #Dentro de CLASSES trabalhamos com METODOS, utilizando o comando DEF para criar um
    #Dentro de um METODO devemos sempre passar um argumento, utilizamos SELF como boa pratica da lingaguem
    #Ao utilizar variaveis dentro de um METODO devemos antes atribuir o SELF a elas
    def __init__(self, cor, modelo, marca, ano, placa, valor):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.placa = placa
        self.valor = valor


    def acelerar(self):
        print("Eu sou a velocidade!")


    def parar(self):
        print("Uno não para!!")


    def buzinar(self):
        print("Foooommmmm" * 10)

    #Podemos criar METODOS para exbir os valores definidos na CLASSE
    #Este METODO tem como problema se caso houver qualquer alteração no nome da classe ou adicionar uma nova variavel o METODO não se atualiza

    #def __str__(self):
        #return f"carro: cor = {self.cor}, modelo = {self.modelo}, marca = {self.marca}"
    
    #Este METODO por sua vez atualiza de junto com as atualizações da classe
    #self.__class__.__name__, utiliza a CLASSE pelo seu nome, qualquer alteração no nome da CLASSE não prejudica o codigo
    #Criamos um FOR para buscar as variaveis e seus valores "CHAVE" "VALOR"
    #Apos percorrer o FOR as variaveis e seus valores são adicionados em uma lista com o self.__dict__
    def __str__(self):
        return  f"{self.__class__.__name__}: {([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

#Atribuindo os valores das variaveis do METODO em uma variavel
car1 = carro("Preto", "Uno", "Fiat", 2000, "FGH-2020", 15000 )
car2 = carro("Cinza", "Gol", "Volkswagen", 2010 , "GOL-2010", 23000)
car1.acelerar()
car1.parar()
car1.buzinar()
#Mostrando os valores da variavel, podemos apenas mostrar valores que desejamos
print(car1.cor, car1.modelo, car1.marca, car1.ano, car1.placa, car1.valor)
print(car1)
print(car2)
 