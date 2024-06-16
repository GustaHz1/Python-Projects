class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    #Usamos o CLASSMETHOD quando há necessidade de um contexto da CLASSE
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    

    #Usamos o STATICMETHOD quando o METODO não necessita de um contexto da CLASSE
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    


p = Pessoa.criar_de_data_nascimento(2005, 5, 30, "Gustavo")
print(p.nome, p.idade)
print(Pessoa.e_maior_idade(19))
print(Pessoa.e_maior_idade(15))