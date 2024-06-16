class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__.items()}"

class Mamifero(Animal):
    #**KW é usado para utilizar todos os valores de uma CLASSE PAI, ao utilizar o **KW em um SUPER qualquer novo valor da CLASSE PAI será adicionado 
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
     def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, **kw):
        super().__init__(**kw)
        #O METODO MRO() é utilizado para mostrar a sequência em que o Python vai percorrer nas classes, passando primeiro por FILHOS,PAIS,AVÔS
        #Utiliza-se este METODO para saber qual CLASSE será executada primeiro e poder mudar algum valor ou saída que deseja 
        print(Ornitorrinco.mro())


#Ao declarar uma variavel recebendo uma CLASSE que utiliza **KW, devemos passar os argumentos com variaveis
gato = Gato(nmr_patas = 2, cor_pelo = "Branco")
print(gato)
ornitorrinco = Ornitorrinco(nmr_patas = 4, cor_pelo = "Preto", cor_bico = "Azul")
print(ornitorrinco)